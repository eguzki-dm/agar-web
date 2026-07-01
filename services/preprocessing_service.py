import numpy as np
from PIL import Image


class PreprocessingService:

    TARGET_SIZE = 224
    PADDING_RATIO = 0.08
    MIN_SIZE_BBOX = 10

    def process_crops(self, image: Image.Image, detections: list[dict]) -> tuple[list, list]:
        img_array = np.array(image.convert("RGB"))
        h_img, w_img = img_array.shape[:2]
        target = self.TARGET_SIZE

        crops_rgba = []
        crops_rgb = []

        for det in detections:
            box = det["box"]
            x1, y1, x2, y2 = map(int, box)

            w = x2 - x1
            h = y2 - y1

            pad = int(max(w, h) * self.PADDING_RATIO)
            x1 = max(0, min(x1 - pad, w_img))
            y1 = max(0, min(y1 - pad, h_img))
            x2 = max(0, min(x2 + pad, w_img))
            y2 = max(0, min(y2 + pad, h_img))

            if (x2 - x1) < self.MIN_SIZE_BBOX or (y2 - y1) < self.MIN_SIZE_BBOX:
                continue

            patch = img_array[y1:y2, x1:x2]
            h_patch, w_patch = patch.shape[:2]

            if h_patch > target or w_patch > target:
                patch = patch[0:min(h_patch, target), 0:min(w_patch, target)]
                h_patch, w_patch = patch.shape[:2]

            canvas = np.zeros((target, target, 3), dtype=np.uint8)

            x_offset = (target - w_patch) // 2
            y_offset = (target - h_patch) // 2

            canvas[y_offset:y_offset + h_patch, x_offset:x_offset + w_patch] = patch

            rgb_img = Image.fromarray(canvas, "RGB")
            crops_rgb.append(rgb_img)

            rgba_img = Image.fromarray(
                np.dstack((canvas, np.full((target, target), 255, dtype=np.uint8))),
                "RGBA"
            )
            crops_rgba.append(rgba_img)

        return crops_rgba, crops_rgb
