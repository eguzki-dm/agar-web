import random
import time
from PIL import Image, ImageDraw

import numpy as np

from config.settings import (
    USE_MOCK,
    SYNTHETIC_IMAGE_WIDTH,
    SYNTHETIC_IMAGE_HEIGHT,
    SYNTHETIC_MIN_COLONIES,
    SYNTHETIC_MAX_COLONIES,
    DETECTION_COLORS,
)


class DetectionService:
    def detect(self, image: Image.Image) -> dict:
        if USE_MOCK:
            return self._mock_detect(image)

        # Placeholder for real YOLO inference
        raise NotImplementedError("Real YOLO detection not yet integrated")

    def generate_synthetic_plate(
        self,
        width: int = SYNTHETIC_IMAGE_WIDTH,
        height: int = SYNTHETIC_IMAGE_HEIGHT,
    ) -> tuple[Image.Image, list[dict]]:
        img = Image.new("RGB", (width, height), (245, 230, 202))
        draw = ImageDraw.Draw(img)

        # Plate border (petri dish)
        border_margin = 30
        plate_color = (230, 210, 180)
        draw.ellipse(
            [border_margin, border_margin, width - border_margin, height - border_margin],
            fill=plate_color,
            outline=(200, 180, 150),
            width=3,
        )

        # Inner agar area
        inner_margin = 60
        agar_color = (245, 232, 200)
        draw.ellipse(
            [inner_margin, inner_margin, width - inner_margin, height - inner_margin],
            fill=agar_color,
        )

        num_colonies = random.randint(SYNTHETIC_MIN_COLONIES, SYNTHETIC_MAX_COLONIES)
        detections = []

        for _ in range(num_colonies):
            # Colony radius between 8 and 30 pixels
            radius = random.randint(8, 30)
            # Keep colonies within the inner agar area
            margin = inner_margin + radius + 10
            cx = random.randint(margin, width - margin)
            cy = random.randint(margin, height - margin)

            # Colony color: cream/white/yellowish tones
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

            # Add slight texture variation (inner circle slightly different shade)
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

            # Bounding box around the colony
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

    def _mock_detect(self, image: Image.Image) -> dict:
        """Simulate detection on a real uploaded image by finding non-background regions."""
        start = time.time()

        img_array = np.array(image.convert("RGB"))
        gray = np.mean(img_array, axis=2)

        # Simple threshold to find colonies (darker regions on light background)
        threshold = 200
        mask = gray < threshold

        if not np.any(mask):
            elapsed = (time.time() - start) * 1000
            return {
                "detections": [],
                "count": 0,
                "time_ms": round(elapsed, 1),
            }

        # Find connected components
        from PIL import ImageFilter

        # Use simple blob detection via connected components
        labeled = np.zeros_like(mask, dtype=int)
        label_num = 0
        connected = _connected_components(mask, labeled)

        detections = []
        h, w = mask.shape
        min_colony_size = 200

        for label_idx in range(1, connected + 1):
            ys, xs = np.where(labeled == label_idx)
            if len(ys) < min_colony_size:
                continue

            x1 = int(xs.min()) - 2
            y1 = int(ys.min()) - 2
            x2 = int(xs.max()) + 2
            y2 = int(ys.max()) + 2

            x1 = max(0, x1)
            y1 = max(0, y1)
            x2 = min(w, x2)
            y2 = min(h, y2)

            confidence = round(random.uniform(0.85, 0.99), 3)
            detections.append({
                "box": [x1, y1, x2, y2],
                "confidence": confidence,
            })

        elapsed = (time.time() - start) * 1000

        return {
            "detections": detections,
            "count": len(detections),
            "time_ms": round(elapsed, 1),
        }

    def sinthetic(self) -> tuple[Image.Image, list[dict]]:
        return self.generate_synthetic_plate()


def _connected_components(binary_mask: np.ndarray, labeled: np.ndarray) -> int:
    """Simple two-pass connected components labeling."""
    label_num = 0
    h, w = binary_mask.shape
    equivalences = {}

    # First pass
    for y in range(h):
        for x in range(w):
            if not binary_mask[y, x]:
                continue

            neighbors = []
            if y > 0 and labeled[y - 1, x] > 0:
                neighbors.append(labeled[y - 1, x])
            if x > 0 and labeled[y, x - 1] > 0:
                neighbors.append(labeled[y, x - 1])

            if not neighbors:
                label_num += 1
                labeled[y, x] = label_num
            else:
                min_label = min(neighbors)
                labeled[y, x] = min_label
                for n in neighbors:
                    if n != min_label:
                        equivalences[n] = min_label

    # Resolve equivalences
    for y in range(h):
        for x in range(w):
            if labeled[y, x] > 0:
                label = labeled[y, x]
                while label in equivalences:
                    label = equivalences[label]
                labeled[y, x] = label

    # Renumber to consecutive
    unique_labels = set()
    for y in range(h):
        for x in range(w):
            if labeled[y, x] > 0:
                unique_labels.add(labeled[y, x])

    renumber = {old: new + 1 for new, old in enumerate(sorted(unique_labels))}
    for y in range(h):
        for x in range(w):
            if labeled[y, x] > 0:
                labeled[y, x] = renumber[labeled[y, x]]

    return len(unique_labels)
