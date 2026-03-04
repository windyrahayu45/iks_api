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

router = APIRouter()

@router.get("/")
def test_iks():
    model = get_model()
    return {"status": "model loaded"}