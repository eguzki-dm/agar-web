import time
import numpy as np
import streamlit as st
import cv2

from app_config.settings import (
    CLASSIFICATION_MODEL_PATH,
    CLASSIFICATION_IMG_SIZE,
    SPECIES,
)

# Model class names (no space after period, as trained)
_MODEL_CLASSES = ["B.subtilis", "C.albicans", "E.coli", "P.aeruginosa", "S.aureus"]

# Mapping: model class name -> display name (add space after period)
_CLASS_TO_SPECIES = {m: s for m, s in zip(_MODEL_CLASSES, SPECIES)}


@st.cache_resource
def _load_classifier():
    import tensorflow as tf
    return tf.keras.models.load_model(CLASSIFICATION_MODEL_PATH)


class ClassificationService:
    def classify(self, processed_crops: list) -> list[dict]:
        model = _load_classifier()
        classifications = []

        for crop in processed_crops:
            img = np.array(crop.convert("RGB"))
            img_resized = cv2.resize(img, (CLASSIFICATION_IMG_SIZE, CLASSIFICATION_IMG_SIZE))
            img_array = img_resized.astype(np.float32) / 255.0
            img_batch = np.expand_dims(img_array, axis=0)

            preds = model.predict(img_batch, verbose=0)[0]
            idx = int(np.argmax(preds))
            conf = float(preds[idx])

            probs = {_CLASS_TO_SPECIES[i]: round(float(preds[i]), 4) for i in range(len(SPECIES))}
            species = _CLASS_TO_SPECIES[idx]

            classifications.append({
                "species": species,
                "confidence": round(conf, 4),
                "probabilities": probs,
            })

        return classifications
