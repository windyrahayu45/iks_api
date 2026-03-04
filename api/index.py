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
import traceback
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Add project root to path
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.insert(0, path)

app = FastAPI(
    title="DTSEN ML Service",
    version="1.0"
)

try:
    from routers import iks, economic, bantuan, anomaly

    app.include_router(
        iks.router,
        prefix="/iks",
        tags=["Indeks Kerentanan Sosial"]
    )

    app.include_router(
        economic.router,
        prefix="/economic",
        tags=["Economic Risk"]
    )

    app.include_router(
        bantuan.router,
        prefix="/bantuan",
        tags=["Rekomendasi Bantuan"]
    )

    app.include_router(
        anomaly.router,
        prefix="/anomaly",
        tags=["Validasi Kelayakan"]
    )

    startup_error = None
except Exception as e:
    startup_error = {
        "error": str(e),
        "trace": traceback.format_exc()
    }

@app.get("/debug-startup")
def debug_startup():
    if startup_error:
        return startup_error
    return {"status": "Startup Successful"}

def handler(request, context):
    from mangum import Mangum
    
    if startup_error:
        # If startup failed, we still want to report it via Mangum if possible
        # or return a direct response if we were using a different handler
        pass

    asgi_handler = Mangum(app)
    return asgi_handler(request, context)

@app.get("/")
def root():
    return {"status": "ROOT WORKING"}


# 👇 Tambahkan ini untuk debug error global
from fastapi.responses import JSONResponse

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc),
            "trace": traceback.format_exc()
        },
    )

