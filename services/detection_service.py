import time
from PIL import Image
import streamlit as st
import numpy as np

from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

from app_config.settings import (
    YOLO_MODEL_PATH,
    YOLO_CONFIDENCE_THRESHOLD,
    YOLO_IOU_THRESHOLD,
    SLICE_SIZE,
    SAHI_OVERLAP_RATIO,
    SAHI_BATCH_SIZE,
    POST_PROCESS_MATCH_THRESHOLD,
    DETECTION_COLORS,
)


@st.cache_resource
def _load_sahi_model():
    return AutoDetectionModel.from_pretrained(
        model_type='ultralytics',
        model_path=YOLO_MODEL_PATH,
        confidence_threshold=YOLO_CONFIDENCE_THRESHOLD,
        device='cpu',
        image_size=SLICE_SIZE,
    )


class DetectionService:
    def detect(self, image: Image.Image) -> dict:
        start = time.time()

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
            perform_standard_pred=True,
            postprocess_class_agnostic=True,
            verbose=0,
        )

        detections = []
        for pred in result.object_prediction_list:
            x1, y1, x2, y2 = map(int, pred.bbox.to_voc_bbox())
            conf = round(float(pred.score.value), 3)
            if (x2 - x1) < 2 or (y2 - y1) < 2:
                continue
            detections.append({
                "box": [x1, y1, x2, y2],
                "confidence": conf,
            })

        elapsed = (time.time() - start) * 1000

        return {
            "detections": detections,
            "count": len(detections),
            "time_ms": round(elapsed, 1),
        }

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
