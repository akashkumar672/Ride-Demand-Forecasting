import pickle
from pathlib import Path
import pandas as pd

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "model.pkl"

def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)

model = load_model()

def predict(data: dict):
    df = pd.DataFrame([data])
    if hasattr(model, 'feature_names_in_'):
        model_features = list(model.feature_names_in_)
        missing = [c for c in model_features if c not in df.columns]
        extra = [c for c in df.columns if c not in model_features]
        if missing:
            raise ValueError(f"Missing required features: {missing}")
        if extra:
            raise ValueError(f"Unexpected features: {extra}")
        df = df[model_features]
    prediction = model.predict(df)
    return prediction[0]