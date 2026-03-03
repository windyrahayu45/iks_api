from pydantic import BaseModel

class EconomicInput(BaseModel):
    economic_score: int
    education_numeric: int
    employment_flag: int
    aid_count: int