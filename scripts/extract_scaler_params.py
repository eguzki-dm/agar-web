import pickle
import json
from pathlib import Path


class _MockScaler:
    def __init__(self):
        self.data_min_ = None
        self.data_max_ = None


class _CustomUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if "sklearn" in module and name == "MinMaxScaler":
            return _MockScaler
        return super().find_class(module, name)


pkl_path = Path("model/Detect/scaler/min_max_scaler.pkl")
params_path = Path("model/Detect/scaler/scaler_params.json")

with open(pkl_path, "rb") as f:
    scaler = _CustomUnpickler(f).load()

params = {
    "data_min_": scaler.data_min_.tolist() if hasattr(scaler.data_min_, "tolist") else list(scaler.data_min_),
    "data_max_": scaler.data_max_.tolist() if hasattr(scaler.data_max_, "tolist") else list(scaler.data_max_),
}

with open(params_path, "w") as f:
    json.dump(params, f, indent=2)

print(f"Params extracted and saved to {params_path}")
print(f"data_min_: {params['data_min_']}")
print(f"data_max_: {params['data_max_']}")
