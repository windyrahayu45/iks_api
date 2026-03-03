from fastapi import APIRouter
from schemas.anomaly_schema import AnomalyInput
from services.anomaly_service import check_anomaly

router = APIRouter()

@router.post("/check")
def anomaly_check(data: AnomalyInput):
    result = check_anomaly(data)
    return result