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

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ROOT WORKING"}