import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "economic_risk_model_v1.pkl"

model = joblib.load(MODEL_PATH)

def predict_economic(data):
    features = np.array([[
        data.economic_score,
        data.education_numeric,
        data.employment_flag,
        data.aid_count
    ]])

    prediction = model.predict(features)[0]
    return round(float(prediction), 2)