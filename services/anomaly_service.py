import joblib
import numpy as np
from pathlib import Path

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = Path(__file__).resolve().parent.parent / "models" / "anomaly_model_v1.pkl"
        _model = joblib.load(model_path)
    return _model

def check_anomaly(data):
    model = get_model()
    features = np.array([[
        data.economic_score,
        data.education_numeric,
        data.employment_flag,
        data.age_bucket,
        data.aid_count
    ]])

    prediction = model.predict(features)[0]
    score = model.decision_function(features)[0]

    return {
        "is_anomaly": True if prediction == -1 else False,
        "anomaly_score": round(float(score), 4)
    }