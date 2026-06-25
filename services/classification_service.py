import random
import time

import numpy as np

from config.settings import USE_MOCK, SPECIES


class ClassificationService:
    def classify(self, processed_crops: list) -> list[dict]:
        if USE_MOCK:
            return self._mock_classify(processed_crops)

        raise NotImplementedError("Real CNN classification not yet integrated")

    def _mock_classify(self, processed_crops: list) -> list[dict]:
        start = time.time()

        classifications = []

        for _ in processed_crops:
            # Random species assignment with dominant species
            n = len(SPECIES)
            probs = np.random.dirichlet(np.ones(n) * 0.5, size=1)[0]

            # Ensure one species is clearly dominant (simulate confident prediction)
            dominant_idx = random.randint(0, n - 1)
            boost = random.uniform(0.1, 0.3)
            probs[dominant_idx] += boost
            probs = probs / probs.sum()

            probabilities = {SPECIES[i]: round(float(probs[i]), 4) for i in range(n)}
            species = SPECIES[dominant_idx]
            confidence = round(float(probs[dominant_idx]), 4)

            classifications.append({
                "species": species,
                "confidence": confidence,
                "probabilities": probabilities,
            })

        elapsed = (time.time() - start) * 1000

        return classifications
