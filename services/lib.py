"""
lib.py — Funciones de procesamiento biológico para segmentación de colonias bacterianas.

Basado en el pipeline de Jarek Pawlowski (microbial-dataset-generation).
Constantes globales para umbrales de filtrado de artefactos y materia oscura.
"""

import numpy as np
import random as rnd
from skimage import color
from skimage.filters import unsharp_mask
from skimage.morphology import dilation, footprint_rectangle
from skimage.segmentation import chan_vese

# ----------------------------------------------------------------
# Constantes globales de filtrado
# ----------------------------------------------------------------
DARK_MATTER_THRESHOLD = 5
DARK_REGIONS_THRESHOLD = 25
COLONIES_THRESHOLD = 30
REMOVE_LABELS = True


def filter_patch(patch):
    """
    Enfoca el parche mediante unsharp_mask y filtra artefactos oscuros
    analizando la luminancia (L) y el canal azul-amarillo (b) del espacio
    CIE L*a*b*. Los píxeles oscuros se reparan con random walk.
    """
    size_x = patch.shape[0]
    size_y = patch.shape[1]
    size_c = patch.shape[2]

    # Canal b (azul-amarillo) en Lab
    b = color.rgb2lab(patch[:, :, :3])[:, :, 2]

    # Enfoque con unsharp mask
    patch = unsharp_mask(patch, radius=100.0, amount=1.5,
                         channel_axis=-1, preserve_range=False)
    patch = np.clip(patch, 0.0, 1.0)

    # Luminancia en Lab
    L = color.rgb2lab(patch[:, :, :3])[:, :, 0]

    if REMOVE_LABELS:
        # Píxeles muy oscuros (etiquetas/bordes de placa) → blanco/transparente
        dark_label = np.logical_and(L <= DARK_MATTER_THRESHOLD,
                                    b < COLONIES_THRESHOLD)
        if size_c == 3:
            patch[dark_label] = [1., 1., 1.]
        elif size_c == 4:
            patch[dark_label] = [1., 1., 1., 0.]

        # Regiones oscuras dentro de la colonia
        mask = np.zeros_like(patch[:, :, 0], dtype=np.uint8)
        mask[np.logical_and.reduce((
            L > DARK_MATTER_THRESHOLD,
            L < DARK_REGIONS_THRESHOLD,
            b < COLONIES_THRESHOLD
        ))] = 1

        # Dilatar máscara para cubrir completamente las regiones oscuras
        dilation_steps = int(np.sqrt(size_x * size_y) / 64)
        if dilation_steps > 16:
            dilation_steps = 16
        for _ in range(dilation_steps):
            mask = dilation(mask)

        # Random walk: reemplaza cada píxel oscuro con el valor
        # del píxel válido más cercano encontrado mediante caminata aleatoria
        where_mask = np.where(mask == 1)
        for i0, j0 in zip(where_mask[0], where_mask[1]):
            i, j = i0, j0
            step = 2
            while mask[i, j] == 1 and step < size_x and step < size_y:
                direction = int(rnd.random() * 4)
                if direction == 0 and i < size_x - step:
                    i += step
                elif direction == 1 and j < size_y - step:
                    j += step
                elif direction == 2 and i > step - 1:
                    i -= step
                elif j > step - 1:
                    j -= step
                step += 2
            patch[i0, j0, :] = patch[i, j, :]

    return patch


def segment_patch(patch):
    """
    Segmenta el parche mediante el algoritmo activo Chan-Vese con
    inicialización de nivel set sinusoidal.
    """
    i = np.arange(patch.shape[0])
    j = np.arange(patch.shape[1])
    ii, jj = np.meshgrid(j, i, sparse=True)
    init_set = (np.sin(ii / 1 * np.pi) * np.sin(jj / 1 * np.pi)) ** 2
    return chan_vese(color.rgb2gray(patch[:, :, :3]),
                     mu=0.5, lambda1=1, lambda2=1,
                     tol=2e-3, max_num_iter=200, dt=0.5,
                     init_level_set=init_set)


def get_alpha_from_segmentation(patch):
    """
    Coordina filter_patch + postpro_filtering + segment_patch y aplica
    dilatación morfológica proporcional al tamaño del parche como margen
    de seguridad.
    """
    patch = filter_patch(patch)
    segmented = segment_patch(patch)
    alpha_matrix = np.zeros_like(segmented, dtype=np.uint8)
    alpha_matrix[segmented] = 255
    dilation_step = max(1, int(np.sqrt(patch.shape[0] ** 2 + patch.shape[1] ** 2) / 50.0))
    alpha_matrix = dilation(alpha_matrix,
                            footprint_rectangle((dilation_step, dilation_step)))
    return alpha_matrix


def get_alpha_from_blending_with_backgroung(
    patch, alpha_from_seg, alpha_from_bboxes
):
    """
    Calcula el color promedio del fondo (Agar) en el espacio Lab y
    mide la distancia euclidiana de los píxeles para generar un degradado
    de opacidad adaptativo en los bordes.

    alpha_from_bboxes debe ser uint8 (0/255), indicando el área total
    del parche candidato.
    """
    patch_lab = color.rgb2lab(patch[:, :, :3])
    bgd_mask = np.logical_and(alpha_from_bboxes == 255,
                              alpha_from_seg == 0)
    background_colors = patch_lab[bgd_mask]

    if background_colors.shape[0] == 0:
        return np.full(patch.shape[:2], 255, dtype=np.uint8)

    bgd_c = [np.mean(background_colors[:, i]) for i in range(3)]
    lab_dist = np.sqrt(
        (patch_lab[:, :, 0] - bgd_c[0]) ** 2 +
        (patch_lab[:, :, 1] - bgd_c[1]) ** 2 +
        (patch_lab[:, :, 2] - bgd_c[2]) ** 2
    )

    lab_dist /= np.amax(lab_dist) + 1e-8
    lab_dist = np.sqrt(np.sin(lab_dist * np.pi / 2.0))
    lab_dist = 0.6 + lab_dist * 0.4
    return (lab_dist * 255).astype(np.uint8)
