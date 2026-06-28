# 🔬 Guía de Arquitectura de Inferencia: Streamlit (Cliente) + Google Colab (Servidor GPU)

Este documento detalla el procedimiento para externalizar el procesamiento pesado de imágenes (YOLOv8 + SAHI) desde el servidor limitado de Streamlit Cloud hacia el entorno con GPU de Google Colab utilizando **FastAPI** y un túnel dinámico con **Ngrok**.

---

## 🏗️ Flujo de Datos del Sistema

1. El usuario accede a la pestaña del **Contador de Colonias** en la App de Streamlit.
2. Introduce la URL pública dinámica generada en Google Colab (ej. `https://xxxx.ngrok-free.app`).
3. Sube la imagen de la placa de Petri a través del widget de Streamlit.
4. Streamlit envía los bytes de la imagen por HTTP POST al servidor de Colab.
5. Colab procesa la imagen con la GPU, calcula las predicciones unificadas y devuelve un JSON plano.
6. Streamlit recibe las coordenadas, renderiza la previsualización y muestra el conteo final sin saturar su memoria RAM.

---

## 🛠️ Paso 1: Configuración en el Servidor (Google Colab)

Añade esta celda al final del cuaderno de investigación y ejecútala. Actuará como el backend del sistema.

```python
# =========================================================================
# BACKEND API: FASTAPI + NGROK FOR STREAMLIT CONNECTION
# =========================================================================

# 1. Instalación de dependencias del servidor
!pip install fastapi uvicorn pyngrok nest-asyncio --quiet

import nest_asyncio
import cv2
import numpy as np
import uvicorn
import json
from fastapi import FastAPI, UploadFile, File
from pyngrok import ngrok

# Permitir bucles asíncronos anidados en entornos Jupyter
nest_asyncio.apply()

app = FastAPI(title="Backend GPU - Colony Counter Engine")

@app.post("/predict")
async def predict_api(file: UploadFile = File(...)):
    """Recibe la placa desde Streamlit, procesa con SAHI y devuelve coordenadas."""
    try:
        # Leer el flujo binario de la imagen entrante
        contents = await file.read()
        nparr = np.frombuffer(contents, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if img is None:
            return {"error": "Could not decode image matrix."}
        
        # Inferencia con SAHI (Función predict_slicing optimizada previamente cargada)
        detections = predict_slicing(sahi_model, img)
        
        # Retornar lista de tuplas en formato JSON nativo: [(x1, y1, x2, y2, conf), ...]
        return {"detections": detections}
        
    except Exception as e:
        return {"error": f"Internal server crash: {str(e)}"}

# =========================================================================
# CONFIGURACIÓN DEL TÚNEL DINÁMICO (NGROK)
# =========================================================================
# Reemplazar con el token obtenido desde dashboard.ngrok.com
NGROK_TOKEN = "TU_NGROK_AUTH_TOKEN_AQUÍ" 
ngrok.set_auth_token(NGROK_TOKEN)

# Limpiar túneles activos redundantes
ngrok.kill()

# Desplegar túnel público HTTP expuesto en el puerto local 8000
public_url = ngrok.connect(8000).public_url

print("=" * 70)
print("🚀 SERVIDOR DE COLAB EMITIENDO EN VIVO")
print("=" * 70)
print(f"🔗 COPIA ESTA URL EN TU STREAMLIT:\n\n   {public_url}\n")
print("=" * 70)
print("⚠️ No detengas la ejecución de esta celda o Streamlit perderá el acceso a la GPU.")

# Lanzar loop del servidor web local
uvicorn.run(app, host="0.0.0.0", port=8000)