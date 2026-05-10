# schemas/customer.py
from pydantic import BaseModel, Field

class CustomerCreate(BaseModel):
    name: str = Field(..., example="John Doe")
    phone: str = Field(..., example="010-1234-5678")
    address: str = Field(..., example="123 Main St, Seoul")

class CustomerRead(BaseModel):
    id: int
    name: str
    phone: str
    address: str

    class Config:
        orm_mode = True
