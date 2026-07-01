import cv2
import numpy as np
from PIL import Image


GAUSSIAN_KERNEL = (5, 5)
GAUSSIAN_SIGMA = 0

GRADIENT_KERNEL_SIZE = (5, 5)
GRADIENT_KERNEL_SHAPE = cv2.MORPH_ELLIPSE

CANNY_LOW = 30
CANNY_HIGH = 90

CLOSE_KERNEL_SIZE = (9, 9)
CLOSE_KERNEL_SHAPE = cv2.MORPH_ELLIPSE

RADIO_RATIO_MIN = 0.28
RADIO_RATIO_MAX = 0.49

BORDER_MARGIN = 0.12

PLATE_REAL_DIAMETER_MM = 90.0


class PlateDetectionService:
    def detect_plate(
        self,
        image: Image.Image | np.ndarray,
        debug: bool = False,
    ) -> dict:
        if isinstance(image, Image.Image):
            img = cv2.cvtColor(np.array(image.convert("RGB")), cv2.COLOR_RGB2BGR)
        else:
            img = image

        h_img, w_img = img.shape[:2]

        # ── 1. Escala de grises + desenfoque ligero ──
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, GAUSSIAN_KERNEL, GAUSSIAN_SIGMA)

        # ── 2. Gradiente morfológico + Canny ──
        kernel_grad = cv2.getStructuringElement(
            GRADIENT_KERNEL_SHAPE, GRADIENT_KERNEL_SIZE
        )
        gradiente = cv2.morphologyEx(blurred, cv2.MORPH_GRADIENT, kernel_grad)
        edges = cv2.Canny(gradiente, CANNY_LOW, CANNY_HIGH)

        kernel_close = cv2.getStructuringElement(
            CLOSE_KERNEL_SHAPE, CLOSE_KERNEL_SIZE
        )
        edges_closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel_close)

        # ── 3. Buscar contornos ──
        contornos, _ = cv2.findContours(
            edges_closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE
        )

        if not contornos:
            return self._empty_result(w_img, h_img)

        # ── 4. Filtrar por tamaño dinámico ──
        dim_minima = min(h_img, w_img)
        radio_maximo = int(dim_minima * RADIO_RATIO_MAX)
        radio_minimo = int(dim_minima * RADIO_RATIO_MIN)

        contornos_validos = []
        for c in contornos:
            (x_c, y_c), r_flotante = cv2.minEnclosingCircle(c)
            r_px = int(r_flotante)

            if not (radio_minimo <= r_px <= radio_maximo):
                continue

            margin_x = w_img * BORDER_MARGIN
            margin_y = h_img * BORDER_MARGIN
            if not (margin_x < x_c < (w_img - margin_x)
                    and margin_y < y_c < (h_img - margin_y)):
                continue

            contornos_validos.append(c)

        if contornos_validos:
            contorno_placa = max(
                contornos_validos, key=lambda c: cv2.minEnclosingCircle(c)[1]
            )
        else:
            contornos_ordenados = sorted(
                contornos, key=cv2.contourArea, reverse=True
            )
            contorno_placa = contornos_ordenados[0]

        # ── 5. Círculo final ──
        (x_flotante, y_flotante), r_flotante = cv2.minEnclosingCircle(contorno_placa)
        x, y, r = int(x_flotante), int(y_flotante), int(r_flotante)

        if r > radio_maximo:
            r = radio_maximo

        # ── 6. Métricas reales ──
        diametro_px = 2 * r
        area_px = np.pi * (r ** 2)
        mm_per_pixel = PLATE_REAL_DIAMETER_MM / diametro_px if diametro_px > 0 else 0.0

        debug_image = None
        if debug:
            output = img.copy()
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)
            cv2.circle(output, (x, y), 5, (0, 0, 255), -1)
            debug_image = Image.fromarray(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))

        return {
            "detected": True,
            "center": (x, y),
            "radius_px": r,
            "diameter_px": diametro_px,
            "area_px": area_px,
            "mm_per_pixel": round(mm_per_pixel, 6),
            "image_size": (w_img, h_img),
            "debug_image": debug_image,
        }

    def _empty_result(self, w: int, h: int) -> dict:
        return {
            "detected": False,
            "center": None,
            "radius_px": None,
            "diameter_px": None,
            "area_px": None,
            "mm_per_pixel": None,
            "image_size": (w, h),
            "debug_image": None,
        }
