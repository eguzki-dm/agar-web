import os
import re
import csv
from PIL import Image


class CropMeasurementService:
    def measure_crops(self, crops: list[Image.Image]) -> list[dict]:
        measurements = []
        for i, crop in enumerate(crops):
            w, h = crop.size
            measurements.append({
                "colony_index": i,
                "width_px": w,
                "height_px": h,
                "total_pixels": w * h,
                "aspect_ratio": round(w / h, 4) if h > 0 else 0,
            })
        return measurements

    @staticmethod
    def measure_crops_from_folder(input_dir: str, output_csv: str):
        registros = []
        extensiones_validas = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")

        if not os.path.exists(input_dir):
            print(f"Error: La ruta '{input_dir}' no existe.")
            return

        print(f"Procesando imágenes en '{input_dir}'...")

        for root, _, files in os.walk(input_dir):
            for nombre_archivo in files:
                if not nombre_archivo.lower().endswith(extensiones_validas):
                    continue

                ruta_completa = os.path.join(root, nombre_archivo)
                base_name = os.path.splitext(nombre_archivo)[0]
                match = re.match(r"(\d+)_(\d+)", base_name)

                if not match:
                    print(f"Advertencia: No se pudo extraer imagen_id/colonia_id de {nombre_archivo}. Saltando.")
                    continue

                imagen_id = match.group(1)
                colonia_id = match.group(2)

                try:
                    img = Image.open(ruta_completa)
                    w, h = img.size
                    registros.append({
                        "imagen_id": imagen_id,
                        "colonia_id": colonia_id,
                        "colonia_px_h": h,
                        "colonia_px_w": w,
                        "colonia_px": w * h,
                    })
                except Exception as e:
                    print(f"No se pudo leer el archivo {nombre_archivo}: {e}")

        import pandas as pd
        df = pd.DataFrame(registros)
        carpeta_destino = os.path.dirname(output_csv)
        if carpeta_destino and not os.path.exists(carpeta_destino):
            os.makedirs(carpeta_destino)
        df.to_csv(output_csv, index=False)

        print(f"CSV guardado en: {output_csv}")
        print(f"Total de imágenes procesadas: {len(registros)}")
