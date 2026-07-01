import numpy as np
from PIL import Image


class PaddingService:

    TARGET_SIZE = 224

    def pad_crops(self, crops: list[Image.Image], target_size: int = None) -> list[Image.Image]:
        if target_size is None:
            target_size = self.TARGET_SIZE
        target = target_size

        padded = []
        for crop in crops:
            img = np.array(crop.convert("RGB"))
            h_orig, w_orig = img.shape[:2]

            if h_orig > target or w_orig > target:
                img = img[0:min(h_orig, target), 0:min(w_orig, target)]
                h_orig, w_orig = img.shape[:2]

            canvas = np.zeros((target, target, 3), dtype=np.uint8)

            x_offset = (target - w_orig) // 2
            y_offset = (target - h_orig) // 2

            canvas[y_offset:y_offset + h_orig, x_offset:x_offset + w_orig] = img

            padded.append(Image.fromarray(canvas, "RGB"))

        return padded
