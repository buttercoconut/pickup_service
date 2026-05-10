# main/app.py
from fastapi import FastAPI
from .routes import customer_router, pickup_request_router, pickup_driver_router
from ..database.engine import init_models

app = FastAPI(title="Pickup Service API")

app.include_router(customer_router)
app.include_router(pickup_request_router)
app.include_router(pickup_driver_router)

@app.on_event("startup")
async def startup_event():
    await init_models()

# Run with: uvicorn backend.main.app:app --reload
