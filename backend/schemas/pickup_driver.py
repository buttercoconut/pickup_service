# schemas/pickup_driver.py
from pydantic import BaseModel, Field

class PickupDriverCreate(BaseModel):
    name: str = Field(..., example="Alice")
    phone: str = Field(..., example="010-9876-5432")
    vehicle_info: str | None = Field(None, example="Toyota Prius")

class PickupDriverRead(BaseModel):
    id: int
    name: str
    phone: str
    vehicle_info: str | None
    is_available: int

    class Config:
        orm_mode = True
