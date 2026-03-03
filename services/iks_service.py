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

_model = None

def get_model():
    global _model
    if _model is None:
        base_dir = os.getcwd()  # ini penting
        model_path = os.path.join(base_dir, "models", "iks_model_v1.pkl")
        print("MODEL PATH:", model_path)
        print("FILE EXISTS:", os.path.exists(model_path))
        _model = joblib.load(model_path)
    return _model

def predict_iks(data):
    model = get_model()

    features = np.array([[
        data.economic_score,
        data.education_numeric,
        data.employment_flag,
        data.age_bucket,
        data.aid_count
    ]])

    prediction = model.predict(features)[0]
    return round(float(prediction), 2)