# import joblib
# import numpy as np
# from pathlib import Path

# _model = None

# def get_model():
#     global _model
#     if _model is None:
#         model_path = Path(__file__).resolve().parent.parent / "models" / "iks_model_v1.pkl"
#         _model = joblib.load(model_path)
#     return _model

# def predict_iks(data):
#     model = get_model()

#     features = np.array([[
#         data.economic_score,
#         data.education_numeric,
#         data.employment_flag,
#         data.age_bucket,
#         data.aid_count
#     ]])

#     prediction = model.predict(features)[0]
#     return round(float(prediction), 2)
import joblib
import numpy as np
import os

from pathlib import Path

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = Path(__file__).resolve().parent.parent / "models" / "iks_model_v1.pkl"
        print("MODEL PATH:", model_path)
        print("FILE EXISTS:", model_path.exists())
        _model = joblib.load(model_path)
    return _model

def predict_iks(data):
    try:
        model = get_model()

        features = np.array([[
            float(data.economic_score or 0),
            float(data.education_numeric or 0),
            float(data.employment_flag or 0),
            float(data.age_bucket or 0),
            float(data.aid_count or 0)
        ]])

        prediction = model.predict(features)[0]
        return round(float(prediction), 2)

    except Exception as e:
        return {
            "error": str(e),
            "received_data": data.dict() if hasattr(data, "dict") else str(data)
        }