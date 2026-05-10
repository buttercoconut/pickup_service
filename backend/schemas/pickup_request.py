# schemas/pickup_request.py
from datetime import datetime
from enum import Enum
from pydantic import BaseModel, Field

class PickupStatus(str, Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class PickupRequestCreate(BaseModel):
    customer_id: int = Field(..., example=1)
    pickup_location: str = Field(..., example="Seoul Station")
    pickup_time: datetime = Field(..., example="2024-05-15T10:30:00Z")
    item_description: str | None = Field(None, example="Large suitcase")

class PickupRequestRead(BaseModel):
    id: int
    customer_id: int
    pickup_location: str
    pickup_time: datetime
    item_description: str | None
    status: PickupStatus
    created_at: datetime
    updated_at: datetime | None

    class Config:
        orm_mode = True

class PickupRequestUpdate(BaseModel):
    pickup_location: str | None = None
    pickup_time: datetime | None = None
    item_description: str | None = None
    status: PickupStatus | None = None
