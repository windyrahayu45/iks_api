# from fastapi import APIRouter
# from schemas.iks_schema import IKSInput
# from services.iks_service import predict_iks

# router = APIRouter()

# @router.post("/predict")
# def predict(data: IKSInput):
#     score = predict_iks(data)

#     return {
#         "iks_score": score
#     }

from fastapi import APIRouter
from services.iks_service import get_model
import numpy as np

router = APIRouter()

@router.get("/")
def test_iks():
    model = get_model()

    # dummy features sesuai jumlah kolom model
    features = np.array([[0, 0, 0, 0, 0]])

    result = model.predict(features)

    return {"result": result.tolist()}