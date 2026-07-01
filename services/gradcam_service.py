import numpy as np
import cv2
from PIL import Image
import tensorflow as tf


class GradCAMService:

    def generate_heatmap(self, model, img_array: np.ndarray, class_idx: int = None) -> np.ndarray:
        gap = model.get_layer("global_average_pooling2d")
        grad_model = tf.keras.models.Model(
            inputs=model.input,
            outputs=[gap.input, model.output]
        )

        with tf.GradientTape() as tape:
            conv_output, preds = grad_model(img_array[np.newaxis, ...], training=False)
            if class_idx is None:
                class_idx = tf.argmax(preds[0])
            loss = preds[:, class_idx]

        grads = tape.gradient(loss, conv_output)
        pooled_grads = tf.reduce_mean(grads, axis=(0, 1, 2))
        heatmap = tf.reduce_sum(tf.multiply(pooled_grads, conv_output[0]), axis=-1)

        heatmap = tf.maximum(heatmap, 0).numpy()
        if np.max(heatmap) > 0:
            heatmap = heatmap / np.max(heatmap)

        heatmap = cv2.resize(heatmap, (img_array.shape[1], img_array.shape[0]))
        heatmap = np.uint8(255 * heatmap)
        heatmap = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        heatmap = cv2.cvtColor(heatmap, cv2.COLOR_BGR2RGB)

        return heatmap

    def overlay(self, image: np.ndarray, heatmap: np.ndarray, alpha: float = 0.4) -> np.ndarray:
        return np.uint8(image * (1 - alpha) + heatmap * alpha)

    def explain_multi(self, images: list[Image.Image], classifications: list[dict]) -> list[dict]:
        from services.classification_service import _load_classifier

        model = _load_classifier()

        species_map = {
            "S. aureus": 4, "B. subtilis": 0, "C. albicans": 1,
            "E. coli": 2, "P. aeruginosa": 3,
        }

        results = []
        for img, cls in zip(images, classifications):
            arr = np.array(img.convert("RGB")).astype(np.float32)
            if arr.shape[:2] != (224, 224):
                arr = cv2.resize(arr, (224, 224))

            class_idx = species_map.get(cls["species"], 0)
            heatmap = self.generate_heatmap(model, arr, class_idx)
            overlay = self.overlay(np.uint8(arr), heatmap)

            results.append({
                "heatmap": Image.fromarray(heatmap, "RGB"),
                "overlay": Image.fromarray(overlay, "RGB"),
            })

        return results
