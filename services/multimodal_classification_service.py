import time
import numpy as np
import streamlit as st
import cv2

from app_config.settings import (
    MULTIMODAL_MODEL_PATH,
    CLASSIFICATION_IMG_SIZE,
    SPECIES,
)

_MODEL_CLASSES = ["B.subtilis", "C.albicans", "E.coli", "P.aeruginosa", "S.aureus"]
_INDEX_TO_SPECIES = [s.replace(".", ". ") for s in _MODEL_CLASSES]


@st.cache_resource
def _load_multimodal_classifier():
    import tensorflow as tf
    return tf.keras.models.load_model(MULTIMODAL_MODEL_PATH)


class MultimodalClassificationService:
    def classify(self, padded_crops: list, scaled_areas: list[float]) -> list[dict]:
        model = _load_multimodal_classifier()

        imgs_array = []
        for crop in padded_crops:
            img = np.array(crop.convert("RGB"))
            img_resized = cv2.resize(img, (CLASSIFICATION_IMG_SIZE, CLASSIFICATION_IMG_SIZE))
            imgs_array.append(img_resized.astype(np.float32))

        imgs_array = np.array(imgs_array)
        areas_array = np.array(scaled_areas, dtype=np.float32).reshape(-1, 1)

        preds = model.predict({"input_imagen": imgs_array, "input_tabular": areas_array}, verbose=0)

        classifications = []
        for i in range(len(preds)):
            probs = preds[i]
            if probs.ndim > 1:
                probs = probs[0]
            idx = int(np.argmax(probs))
            conf = float(probs[idx])

            prob_dict = {_INDEX_TO_SPECIES[j]: round(float(probs[j]), 4) for j in range(len(SPECIES))}
            species = _INDEX_TO_SPECIES[idx]

            classifications.append({
                "species": species,
                "confidence": round(conf, 4),
                "probabilities": prob_dict,
            })

        return classifications
