from fastapi import APIRouter
from schemas.iks_schema import IKSInput
from services.iks_service import predict_iks

router = APIRouter()

@router.post("/predict")
def predict(data: IKSInput):
    score = predict_iks(data)

    return {
        "iks_score": score
    }

