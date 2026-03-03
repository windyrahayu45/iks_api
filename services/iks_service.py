import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "iks_model_v1.pkl"

model = joblib.load(MODEL_PATH)

def predict_iks(data):
    features = np.array([[
        data.economic_score,
        data.education_numeric,
        data.employment_flag,
        data.age_bucket,
        data.aid_count
    ]])

    prediction = model.predict(features)[0]
    return round(float(prediction), 2)