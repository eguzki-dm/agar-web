import time
from PIL import Image, ImageDraw
import streamlit as st
import numpy as np
import cv2

from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

from app_config.settings import (
    YOLO_MODEL_PATH,
    YOLO_MODEL_RESIZE_PATH,
    YOLO_CONFIDENCE_THRESHOLD,
    YOLO_IOU_THRESHOLD,
    SLICE_SIZE,
    SAHI_OVERLAP_RATIO,
    SAHI_BATCH_SIZE,
    POST_PROCESS_MATCH_THRESHOLD,
    LETTERBOX_SIZE,
    DETECTION_COLORS,
)


@st.cache_resource
def _load_sahi_model():
    return AutoDetectionModel.from_pretrained(
        model_type='ultralytics',
        model_path=YOLO_MODEL_PATH,
        confidence_threshold=0.1,
        device='cpu',
        image_size=SLICE_SIZE,
    )


@st.cache_resource
def _load_resize_model():
    from ultralytics import YOLO
    return YOLO(YOLO_MODEL_RESIZE_PATH)


def _letterbox_image(img: np.ndarray, target_size: int = LETTERBOX_SIZE) -> tuple:
    h, w = img.shape[:2]
    scale = min(target_size / w, target_size / h)
    new_w = int(w * scale)
    new_h = int(h * scale)
    resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_LINEAR)
    pad_left = (target_size - new_w) // 2
    pad_top = (target_size - new_h) // 2
    padded = cv2.copyMakeBorder(
        resized, pad_top, target_size - new_h - pad_top,
        pad_left, target_size - new_w - pad_left,
        cv2.BORDER_CONSTANT, value=(114, 114, 114),
    )
    return padded, scale, pad_left, pad_top


class DetectionService:
    def detect(self, image: Image.Image, confidence_threshold: float | None = None) -> dict:
        threshold = confidence_threshold if confidence_threshold is not None else YOLO_CONFIDENCE_THRESHOLD
        start = time.time()
        w, h = image.size

        if w >= SLICE_SIZE and h >= SLICE_SIZE:
            detections = self._detect_slicing(image, threshold)
        else:
            detections = self._detect_resize(image, threshold)

        elapsed = time.time() - start

        return {
            "detections": detections,
            "count": len(detections),
            "time_s": round(elapsed, 2),
        }

    def _detect_slicing(self, image: Image.Image, confidence_threshold: float) -> list[dict]:
        model = _load_sahi_model()
        img_array = np.array(image.convert("RGB"))

        result = get_sliced_prediction(
            img_array,
            model,
            slice_height=SLICE_SIZE,
            slice_width=SLICE_SIZE,
            overlap_height_ratio=SAHI_OVERLAP_RATIO,
            overlap_width_ratio=SAHI_OVERLAP_RATIO,
            batch_size=SAHI_BATCH_SIZE,
            postprocess_type='GREEDYNMM',
            postprocess_match_metric='IOU',
            postprocess_match_threshold=POST_PROCESS_MATCH_THRESHOLD,
            perform_standard_pred=False,
            postprocess_class_agnostic=True,
            verbose=0,
        )

        detections = []
        for pred in result.object_prediction_list:
            x1, y1, x2, y2 = map(int, pred.bbox.to_voc_bbox())
            conf = round(float(pred.score.value), 3)
            if conf < confidence_threshold:
                continue
            if (x2 - x1) < 2 or (y2 - y1) < 2:
                continue
            detections.append({
                "box": [x1, y1, x2, y2],
                "confidence": conf,
            })
        return detections

    def _detect_resize(self, image: Image.Image, confidence_threshold: float) -> list[dict]:
        model = _load_resize_model()
        img_bgr = cv2.cvtColor(np.array(image.convert("RGB")), cv2.COLOR_RGB2BGR)
        h, w = img_bgr.shape[:2]

        letterboxed, scale, pad_left, pad_top = _letterbox_image(img_bgr)

        results = model.predict(
            letterboxed,
            conf=confidence_threshold,
            iou=YOLO_IOU_THRESHOLD,
            verbose=False,
        )

        detections = []
        for r in results:
            if r.boxes is None:
                continue
            for box in r.boxes:
                xc, yc, bw, bh = box.xywhn[0].tolist()
                conf = float(box.conf[0])
                x_center_px = xc * LETTERBOX_SIZE
                y_center_px = yc * LETTERBOX_SIZE
                bw_px = bw * LETTERBOX_SIZE
                bh_px = bh * LETTERBOX_SIZE
                x1_l = x_center_px - bw_px / 2
                y1_l = y_center_px - bh_px / 2
                x2_l = x_center_px + bw_px / 2
                y2_l = y_center_px + bh_px / 2
                x1 = int((x1_l - pad_left) / scale)
                y1 = int((y1_l - pad_top) / scale)
                x2 = int((x2_l - pad_left) / scale)
                y2 = int((y2_l - pad_top) / scale)
                x1 = max(0, min(x1, w))
                y1 = max(0, min(y1, h))
                x2 = max(0, min(x2, w))
                y2 = max(0, min(y2, h))
                if (x2 - x1) < 2 or (y2 - y1) < 2:
                    continue
                detections.append({
                    "box": [x1, y1, x2, y2],
                    "confidence": round(conf, 3),
                })
        return detections

    def draw_boxes(
        self,
        image: Image.Image,
        detections: list[dict],
    ) -> Image.Image:
        img_copy = image.copy()
        draw = ImageDraw.Draw(img_copy)

        for i, det in enumerate(detections):
            box = det["box"]
            color = DETECTION_COLORS[i % len(DETECTION_COLORS)]
            draw.rectangle(box, outline=color, width=2)

            label = f"#{i + 1} ({det['confidence']:.2f})"
            x1, y1, _, _ = box
            draw.text((x1 + 2, y1 - 12), label, fill=color)

        return img_copy
