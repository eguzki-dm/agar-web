from PIL import Image
import numpy as np

from app_config.settings import USE_MOCK


class PreprocessingService:
    def crop_colony(self, image: Image.Image, box: list[int]) -> Image.Image:
        x1, y1, x2, y2 = box
        return image.crop((x1, y1, x2, y2))

    def apply_black_background(self, crop: Image.Image) -> Image.Image:
        """Convierte el fondo blanco/beige del crop en negro, manteniendo la colonia visible."""
        if crop.mode != "RGB":
            crop = crop.convert("RGB")

        img_array = np.array(crop)
        gray = np.mean(img_array, axis=2)

        threshold = 200
        mask = gray > threshold

        img_array[mask] = [0, 0, 0]

        return Image.fromarray(img_array)

    def process_crops(self, image: Image.Image, detections: list[dict]) -> tuple[list, list]:
        crops = []
        processed_crops = []

        for det in detections:
            box = det["box"]
            crop = self.crop_colony(image, box)
            processed = self.apply_black_background(crop)
            crops.append(crop)
            processed_crops.append(processed)

        return crops, processed_crops
