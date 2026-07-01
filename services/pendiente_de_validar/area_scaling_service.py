import json
from pathlib import Path


class AreaScalingService:

    PARAMS_PATH = Path("model/Detect/scaler/scaler_params.json")

    def __init__(self):
        with open(self.PARAMS_PATH) as f:
            params = json.load(f)
        self.data_min = params["data_min_"][0]
        self.data_max = params["data_max_"][0]
        self.range = self.data_max - self.data_min

    def pixel_area_to_mm2(self, colonia_px: float, mm_per_pixel: float) -> float:
        return colonia_px * (mm_per_pixel ** 2)

    def scale(self, area_mm2: float) -> float:
        return (area_mm2 - self.data_min) / self.range

    def process_crops(
        self, crop_measurements: list[dict], mm_per_pixel: float
    ) -> list[dict]:
        for m in crop_measurements:
            area_mm2 = self.pixel_area_to_mm2(m["total_pixels"], mm_per_pixel)
            scaled = self.scale(area_mm2)
            m["area_mm2"] = round(area_mm2, 4)
            m["area_scaled"] = round(scaled, 4)
        return crop_measurements
