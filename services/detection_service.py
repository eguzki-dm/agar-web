import random
import time
import cv2
import numpy as np
from PIL import Image, ImageDraw
import streamlit as st

from ultralytics import YOLO

from config.settings import (
    YOLO_MODEL_PATH,
    YOLO_CONFIDENCE_THRESHOLD,
    YOLO_IOU_THRESHOLD,
    SLICE_SIZE,
    STRIDE,
    SYNTHETIC_IMAGE_WIDTH,
    SYNTHETIC_IMAGE_HEIGHT,
    SYNTHETIC_MIN_COLONIES,
    SYNTHETIC_MAX_COLONIES,
    DETECTION_COLORS,
)


def _compute_iou(box1, box2):
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])
    inter = max(0, x2 - x1) * max(0, y2 - y1)
    area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
    area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
    return inter / (area1 + area2 - inter + 1e-6)


def _nms(detections, iou_threshold=YOLO_IOU_THRESHOLD):
    if not detections:
        return []
    dets = sorted(detections, key=lambda d: d["confidence"], reverse=True)
    kept = []
    for d in dets:
        keep = True
        for k in kept:
            if _compute_iou(d["box"], k["box"]) > iou_threshold:
                keep = False
                break
        if keep:
            kept.append(d)
    return kept


def _slice_image(image, slice_size=SLICE_SIZE, stride=STRIDE):
    h, w = image.shape[:2]
    tiles = []
    for y in range(0, max(h - slice_size + 1, 1), stride):
        for x in range(0, max(w - slice_size + 1, 1), stride):
            y_end = min(y + slice_size, h)
            x_end = min(x + slice_size, w)
            if y_end - y < slice_size:
                y = max(0, h - slice_size)
                y_end = h
            if x_end - x < slice_size:
                x = max(0, w - slice_size)
                x_end = w
            tile = image[y:y_end, x:x_end]
            if tile.shape[0] < slice_size or tile.shape[1] < slice_size:
                tile = cv2.copyMakeBorder(
                    tile,
                    0, slice_size - tile.shape[0],
                    0, slice_size - tile.shape[1],
                    cv2.BORDER_CONSTANT,
                    value=(0, 0, 0),
                )
            tiles.append({
                "tile": tile,
                "offset_x": x,
                "offset_y": y,
            })
    return tiles


@st.cache_resource
def _load_model():
    return YOLO(YOLO_MODEL_PATH)


class DetectionService:
    def detect(self, image: Image.Image) -> dict:
        start = time.time()

        model = _load_model()
        img_array = np.array(image.convert("RGB"))
        tiles = _slice_image(img_array)

        all_detections = []
        for t in tiles:
            tile_img = t["tile"]
            ox, oy = t["offset_x"], t["offset_y"]
            results = model(
                tile_img,
                conf=YOLO_CONFIDENCE_THRESHOLD,
                iou=0.5,
                verbose=False,
            )
            for r in results:
                boxes = r.boxes
                if boxes is None:
                    continue
                xyxy = boxes.xyxy.cpu().numpy()
                confs = boxes.conf.cpu().numpy()
                for box, conf in zip(xyxy, confs):
                    x1, y1, x2, y2 = map(float, box)
                    all_detections.append({
                        "box": [
                            int(x1 + ox),
                            int(y1 + oy),
                            int(x2 + ox),
                            int(y2 + oy),
                        ],
                        "confidence": round(float(conf), 3),
                    })

        all_detections = _nms(all_detections)

        elapsed = (time.time() - start) * 1000

        return {
            "detections": all_detections,
            "count": len(all_detections),
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
