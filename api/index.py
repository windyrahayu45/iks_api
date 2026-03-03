# from fastapi import FastAPI
# from routers import iks,economic, bantuan,anomaly

# app = FastAPI(
#     title="DTSEN ML Service",
#     version="1.0"
# )

# app.include_router(
#     iks.router,
#     prefix="/iks",
#     tags=["Indeks Kerentanan Sosial"]
# )

# # Use Case 2
# app.include_router(
#     economic.router,
#     prefix="/economic",
#     tags=["Economic Risk"]
# )

# app.include_router(
#     bantuan.router,
#     prefix="/bantuan",
#     tags=["Rekomendasi Bantuan"]
# )

# app.include_router(
#     anomaly.router,
#     prefix="/anomaly",
#     tags=["Validasi Kelayakan"]
# )

# @app.get("/")
# def root():
#     return {"status": "DTSEN ML Service Running"}

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from routers import iks

app = FastAPI()

app.include_router(
    iks.router,
    prefix="/iks"
)



@app.get("/")
def root():
    return {"status": "ROOT WORKING"}

from pathlib import Path

def get_model():
    model_path = Path(__file__).resolve().parent.parent / "models" / "iks_model_v1.pkl"
    print("MODEL PATH:", model_path)
    print("FILE EXISTS:", model_path.exists())
    return joblib.load(model_path)