import joblib
import numpy as np
from pathlib import Path

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = Path(__file__).resolve().parent.parent / "models" / "economic_risk_model_v1.pkl"
        _model = joblib.load(model_path)
    return _model

def predict_economic(data):
    model = get_model()
    features = np.array([[
        data.economic_score,
        data.education_numeric,
        data.employment_flag,
        data.aid_count
    ]])

    prediction = model.predict(features)[0]
    return round(float(prediction), 2)