import random
import time
from PIL import Image, ImageDraw
import streamlit as st
import numpy as np

from sahi import AutoDetectionModel
from sahi.predict import get_sliced_prediction

from config.settings import (
    YOLO_MODEL_PATH,
    YOLO_CONFIDENCE_THRESHOLD,
    YOLO_IOU_THRESHOLD,
    SLICE_SIZE,
    SAHI_OVERLAP_RATIO,
    SAHI_BATCH_SIZE,
    POST_PROCESS_MATCH_THRESHOLD,
    SYNTHETIC_IMAGE_WIDTH,
    SYNTHETIC_IMAGE_HEIGHT,
    SYNTHETIC_MIN_COLONIES,
    SYNTHETIC_MAX_COLONIES,
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

    def generate_synthetic_plate(
        self,
        width: int = SYNTHETIC_IMAGE_WIDTH,
        height: int = SYNTHETIC_IMAGE_HEIGHT,
    ) -> tuple[Image.Image, list[dict]]:
        img = Image.new("RGB", (width, height), (245, 230, 202))
        draw = ImageDraw.Draw(img)

        border_margin = 30
        plate_color = (230, 210, 180)
        draw.ellipse(
            [border_margin, border_margin, width - border_margin, height - border_margin],
            fill=plate_color,
            outline=(200, 180, 150),
            width=3,
        )

        inner_margin = 60
        agar_color = (245, 232, 200)
        draw.ellipse(
            [inner_margin, inner_margin, width - inner_margin, height - inner_margin],
            fill=agar_color,
        )

        num_colonies = random.randint(SYNTHETIC_MIN_COLONIES, SYNTHETIC_MAX_COLONIES)
        detections = []

        for _ in range(num_colonies):
            radius = random.randint(8, 30)
            margin = inner_margin + radius + 10
            cx = random.randint(margin, width - margin)
            cy = random.randint(margin, height - margin)

            colony_color = (
                random.randint(220, 255),
                random.randint(200, 240),
                random.randint(170, 220),
            )

            draw.ellipse(
                [cx - radius, cy - radius, cx + radius, cy + radius],
                fill=colony_color,
                outline=(180, 160, 130),
                width=1,
            )

            inner_radius = radius * random.randint(3, 6) // 10
            inner_color = (
                min(255, colony_color[0] + 10),
                min(255, colony_color[1] + 10),
                min(255, colony_color[2] + 5),
            )
            draw.ellipse(
                [cx - inner_radius, cy - inner_radius, cx + inner_radius, cy + inner_radius],
                fill=inner_color,
            )

            margin_box = 2
            x1 = cx - radius - margin_box
            y1 = cy - radius - margin_box
            x2 = cx + radius + margin_box
            y2 = cy + radius + margin_box

            detections.append({
                "box": [x1, y1, x2, y2],
                "confidence": round(random.uniform(0.85, 0.99), 3),
            })

        return img, detections

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

    def synthetic(self) -> tuple[Image.Image, list[dict]]:
        return self.generate_synthetic_plate()
