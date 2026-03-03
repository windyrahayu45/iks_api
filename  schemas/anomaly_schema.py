from pydantic import BaseModel

class AnomalyInput(BaseModel):
    economic_score: int
    education_numeric: int
    employment_flag: int
    age_bucket: int
    aid_count: int