from pydantic import BaseModel

class BantuanInput(BaseModel):
    economic_score: int
    education_numeric: int
    employment_flag: int
    age_bucket: int
    aid_count: int

    penerima_bpnt: bool
    penerima_bst: bool
    penerima_pkh: bool
    penerima_sembako: bool
    penerima_prakerja: bool
    penerima_kur: bool
    penerima_cbp: bool