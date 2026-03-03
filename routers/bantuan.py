from fastapi import APIRouter
from schemas.bantuan_schema import BantuanInput
from services.bantuan_service import recommend_bantuan

router = APIRouter()

@router.post("/recommend")
def recommend(data: BantuanInput):
    result = recommend_bantuan(data)
    return result