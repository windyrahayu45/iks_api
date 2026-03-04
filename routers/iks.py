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
from services import iks_service

router = APIRouter()

print("IKS ROUTER IMPORTED")

@router.get("/")
def test_iks():
    return {"iks": "router working"}