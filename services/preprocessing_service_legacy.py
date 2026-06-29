import cv2
import numpy as np
from PIL import Image


class PreprocessingService:
    MIN_SIZE_BBOX = 10
    SAFETY_MARGIN = 1.05
    TARGET_SIZE_CNN = 224

    def _get_alpha_from_segmentation(self, patch_rgb: np.ndarray) -> np.ndarray:
        gray = cv2.cvtColor(patch_rgb, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, mask = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        if mask[0, 0] == 255:
            mask = cv2.bitwise_not(mask)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel, iterations=2)
        return mask

    def _get_alpha_from_blending_with_background(self, patch_rgb: np.ndarray, alpha_seg: np.ndarray) -> np.ndarray:
        h, w = patch_rgb.shape[:2]
        corners = np.array([
            patch_rgb[0, 0], patch_rgb[0, w - 1],
            patch_rgb[h - 1, 0], patch_rgb[h - 1, w - 1]
        ])
        background_color = np.mean(corners, axis=0)

        dist = np.linalg.norm(patch_rgb.astype(np.float32) - background_color.astype(np.float32), axis=2)
        dist_norm = cv2.normalize(dist, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)

        blended_alpha = cv2.bitwise_and(dist_norm, alpha_seg)
        return blended_alpha

    def _process_crop_absolute_scale(self, crop_4ch: np.ndarray, canvas_size: int, final_size: int) -> np.ndarray:
        h, w = crop_4ch.shape[:2]
        canvas = np.zeros((canvas_size, canvas_size, 4), dtype=np.uint8)

        y_offset = (canvas_size - h) // 2
        x_offset = (canvas_size - w) // 2

        y1, y2 = max(0, y_offset), min(canvas_size, y_offset + h)
        x1, x2 = max(0, x_offset), min(canvas_size, x_offset + w)
        cy1, cy2 = max(0, -y_offset), max(0, -y_offset) + (y2 - y1)
        cx1, cx2 = max(0, -x_offset), max(0, -x_offset) + (x2 - x1)

        canvas[y1:y2, x1:x2] = crop_4ch[cy1:cy2, cx1:cx2]
        final_image = cv2.resize(canvas, (final_size, final_size), interpolation=cv2.INTER_AREA)
        return final_image

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

    def crop_colony(self, image: Image.Image, box: list[int]) -> Image.Image:
        x1, y1, x2, y2 = box
        return image.crop((x1, y1, x2, y2))

    def apply_black_background(self, crop_rgba: np.ndarray) -> Image.Image:
        bgr = crop_rgba[:, :, :3]
        alpha = crop_rgba[:, :, 3]
        alpha_norm = alpha.astype(np.float32) / 255.0
        result = np.uint8(bgr * alpha_norm[:, :, None])
        return Image.fromarray(result, "RGB")

    def process_crops(self, image: Image.Image, detections: list[dict]) -> tuple[list, list]:
        canvas_size = self._compute_canvas_size(detections)
        img_array = np.array(image.convert("RGB"))

        crops = []
        processed_crops = []

        for det in detections:
            box = det["box"]
            x1, y1, x2, y2 = map(int, box)
            h_img, w_img = img_array.shape[:2]

            x1 = max(0, min(x1, w_img))
            y1 = max(0, min(y1, h_img))
            x2 = max(0, min(x2, w_img))
            y2 = max(0, min(y2, h_img))

            if (x2 - x1) < self.MIN_SIZE_BBOX or (y2 - y1) < self.MIN_SIZE_BBOX:
                continue

            patch_rgb = img_array[y1:y2, x1:x2]

            alpha_seg = self._get_alpha_from_segmentation(patch_rgb)
            alpha_blend = self._get_alpha_from_blending_with_background(patch_rgb, alpha_seg)

            alpha_matrix = ((alpha_seg.astype(np.float32) / 255.0) *
                            (alpha_blend.astype(np.float32) / 255.0) * 255.0).astype(np.uint8)

            crop_4ch = np.dstack((patch_rgb, alpha_matrix))
            crop_scaled = self._process_crop_absolute_scale(crop_4ch, canvas_size, self.TARGET_SIZE_CNN)

            crops.append(Image.fromarray(crop_scaled, "RGBA"))
            processed_crops.append(self.apply_black_background(crop_scaled))

        return crops, processed_crops
