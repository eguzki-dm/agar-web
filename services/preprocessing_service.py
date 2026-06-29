import cv2
import numpy as np
from PIL import Image

from lib import (
    get_alpha_from_segmentation,
    get_alpha_from_blending_with_backgroung,
)


class PreprocessingService:

    MIN_SIZE_BBOX = 10
    SAFETY_MARGIN = 1.05
    TARGET_SIZE_CNN = 224

    # =========================================================
    # EXACT SAME AS V3
    # =========================================================

    def _process_crop_absolute_scale(self, crop_4ch: np.ndarray, canvas_size: int, final_size: int) -> np.ndarray:
        h, w = crop_4ch.shape[:2]
        canvas = np.zeros((canvas_size, canvas_size, 4), dtype=np.uint8)

        y_offset = (canvas_size - h) // 2
        x_offset = (canvas_size - w) // 2

        y1 = max(0, y_offset)
        y2 = min(canvas_size, y_offset + h)
        x1 = max(0, x_offset)
        x2 = min(canvas_size, x_offset + w)

        cy1 = max(0, -y_offset)
        cy2 = cy1 + (y2 - y1)
        cx1 = max(0, -x_offset)
        cx2 = cx1 + (x2 - x1)

        canvas[y1:y2, x1:x2] = crop_4ch[cy1:cy2, cx1:cx2]

        return cv2.resize(canvas, (final_size, final_size), interpolation=cv2.INTER_AREA)

    # =========================================================
    # CANVAS SIZE = SAME LOGIC AS V3 (percentile global)
    # =========================================================

    def _compute_canvas_size(self, detections: list[dict]) -> int:
        dims = []

        for det in detections:
            box = det["box"]
            w = box[2] - box[0]
            h = box[3] - box[1]

            if w >= self.MIN_SIZE_BBOX and h >= self.MIN_SIZE_BBOX:
                dims.append(max(int(w), int(h)))

        if not dims:
            return self.TARGET_SIZE_CNN

        canvas_size = int(np.percentile(dims, 99.5) * self.SAFETY_MARGIN)
        return canvas_size

    # =========================================================
    # MAIN PIPELINE (V3 EXACT MATCH)
    # =========================================================

    def process_crops(self, image: Image.Image, detections: list[dict]) -> tuple[list, list]:

        canvas_size = self._compute_canvas_size(detections)
        img = np.array(image.convert("RGB"))

        crops = []
        processed = []

        for det in detections:

            x1, y1, x2, y2 = map(int, det["box"])
            h_img, w_img = img.shape[:2]

            pad = int(max(x2 - x1, y2 - y1) * 0.08)

            x1 = max(0, min(x1 - pad, w_img))
            y1 = max(0, min(y1 - pad, h_img))
            x2 = max(0, min(x2 + pad, w_img))
            y2 = max(0, min(y2 + pad, h_img))

            if (x2 - x1) < self.MIN_SIZE_BBOX or (y2 - y1) < self.MIN_SIZE_BBOX:
                continue

            patch_rgb = img[y1:y2, x1:x2]

            # =====================================================
            # 1. EXACT SAME SEGMENTATION (Chan-Vese from lib)
            # =====================================================
            alpha_seg = get_alpha_from_segmentation(patch_rgb)

            # =====================================================
            # 2. EXACT SAME BLENDING (agar background model)
            # =====================================================
            alpha_bboxes = np.ones_like(alpha_seg, dtype=np.uint8) * 255

            alpha_blend = get_alpha_from_blending_with_backgroung(
                patch_rgb,
                alpha_seg,
                alpha_bboxes,
            )

            # =====================================================
            # 3. EXACT SAME COMBINATION
            # =====================================================
            alpha = (
                (alpha_seg.astype(np.float32) / 255.0)
                * (alpha_blend.astype(np.float32) / 255.0)
                * 255.0
            ).astype(np.uint8)

            # =====================================================
            # 4. RGBA + canvas
            # =====================================================
            crop_4ch = np.dstack((patch_rgb, alpha))

            final = self._process_crop_absolute_scale(
                crop_4ch,
                canvas_size,
                self.TARGET_SIZE_CNN,
            )

            crops.append(Image.fromarray(final, "RGBA"))

            # black background version EXACT SAME LOGIC AS BEFORE
            rgb = final[:, :, :3]
            a = final[:, :, 3].astype(np.float32) / 255.0
            processed.append(Image.fromarray((rgb * a[:, :, None]).astype(np.uint8), "RGB"))

        return crops, processed
