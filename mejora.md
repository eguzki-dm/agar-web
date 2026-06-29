# Propuesta de Normalización de Escala y Preprocesamiento para el Proyecto Agar

## 1. Introducción y Problema Técnico
En el **Proyecto Agar**, la clasificación de especies bacterianas depende de manera crítica de la morfología de sus colonias. Uno de los factores bioclimáticos y morfológicos más determinantes es el **tamaño real de la colonia** en la placa de Petri (por ejemplo, colonias puntiformes de *Micrococcus* vs. colonias extendidas de *Bacillus*).

Cuando se preparan las imágenes para una Red Neuronal Convolucional (CNN), el enfoque tradicional de reescalado directo (`resize` forzado a un tamaño fijo como $64 \times 64$) **destruye la información de escala**. Una colonia pequeña de $32 \times 32\text{ px}$ se estiraría afectando a su textura, mientras que una de $52 \times 52\text{ px}$ se reduciría, haciendo que la CNN pierda la capacidad de diferenciar las especies por su tamaño biológico real.

## 2. La Idea: Calibración Métrica Basada en la Placa (90 mm)
La solución propuesta consiste en aprovechar un elemento físico de dimensiones constantes en el experimento: **el diámetro de la placa de Petri (90 mm)**. 

Al detectar la placa en la imagen, podemos establecer una equivalencia matemática exacta entre píxeles y milímetros ($\text{px/mm}$), garantizando que el tamaño de la colonia se preserve de forma idéntica sin importar la distancia de la cámara o el zoom.

## 3. Flujo de Trabajo del Algoritmo

1. **Detección de la Placa de Petri:** Se identifica el contorno circular de la placa en la imagen para obtener su diámetro en píxeles (placa en px).
2. **Cálculo de la Escala Absoluta:** Escala (px/mm) = placa px/ 90 mm
3. **Reescalado Proporcional de la Colonia:** Se define una proporción estándar deseada para la CNN (por ejemplo, 10 píxeles por cada 1 mm). El recorte de la colonia se redimensiona siguiendo esta escala real, manteniendo sus proporciones nativas.
4. **Padding (Acolchado) Centrado:** La colonia escalada se inserta en el centro de un "lienzo" negro de tamaño fijo (ej. $128 \times 128\text{ px}$) requerido por la arquitectura de la CNN.

## 4. Implementación de Referencia (Python + OpenCV)

A continuación se muestra el código en Python para integrar este proceso en el *pipeline* de datos:

```python
import cv2
import numpy as np

def pad_to_target(image, target_size=(128, 128)):
    """Añade un borde negro (padding) para centrar la imagen en un tamaño fijo."""
    h, w = image.shape[:2]
    top = (target_size[0] - h) // 2
    bottom = target_size[0] - h - top
    left = (target_size[1] - w) // 2
    right = target_size[1] - w - left
    
    return cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=[0, 0, 0])

def preprocesar_colonia_agar(imagen_original, diametro_placa_px, bbox_colonia):
    """
    Preprocesa la colonia manteniendo la escala biológica real en mm.
    
    Argumentos:
        imagen_original: Matriz de la imagen completa.
        diametro_placa_px: Diámetro en píxeles de la placa detectada.
        bbox_colonia: Tupla (x, y, w, h) con las coordenadas de la colonia.
    """
    # 1. Calcular la escala real de la fotografía
    px_per_mm = diametro_placa_px / 90.0
    
    # 2. Extraer el recorte (ROI) de la colonia
    x, y, w, h = bbox_colonia
    recorte = imagen_original[y:y+h, x:x+w]
    
    # 3. Definir el estándar para la CNN (Ej: 10 píxeles = 1 mm)
    PROPORCION_ESTANDAR = 10.0  
    
    nuevo_w = int((w / px_per_mm) * PROPORCION_ESTANDAR)
    nuevo_h = int((h / px_per_mm) * PROPORCION_ESTANDAR)
    
    # Reescalado que preserva la proporción real
    colonia_escalada = cv2.resize(recorte, (nuevo_w, nuevo_h))
    
    # 4. Aplicar padding para el molde fijo de la CNN
    imagen_final_cnn = pad_to_target(colonia_escalada, target_size=(128, 128))
    
    # 5. Extracción de variables numéricas adicionales (Metadatos)
    ancho_mm = w / px_per_mm
    alto_mm = h / px_per_mm
    
    return imagen_final_cnn, (ancho_mm, alto_mm)
