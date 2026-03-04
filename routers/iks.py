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

# from fastapi import APIRouter, Request
# from services.iks_service import predict_iks

# router = APIRouter()

# @router.post("/predict")
# async def predict(request: Request):
#     body = await request.json()

#     class Dummy:
#         pass

#     data = Dummy()
#     data.economic_score = body.get("economic_score", 0)
#     data.education_numeric = body.get("education_numeric", 0)
#     data.employment_flag = body.get("employment_flag", 0)
#     data.age_bucket = body.get("age_bucket", 0)
#     data.aid_count = body.get("aid_count", 0)

#     score = predict_iks(data)

#     return {"iks_score": score}