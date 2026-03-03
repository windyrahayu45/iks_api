from fastapi import APIRouter
from schemas.economic_schema import EconomicInput
from services.economic_service import predict_economic

router = APIRouter()

@router.post("/predict")
def predict(data: EconomicInput):
    score = predict_economic(data)

    return {
        "economic_risk_score": score
    }