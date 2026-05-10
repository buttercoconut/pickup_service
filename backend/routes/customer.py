# routes/customer.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..config import settings
from ..models import Customer
from ..schemas import CustomerCreate, CustomerRead
from ..database import get_db

router = APIRouter(prefix="/customers", tags=["customers"])

@router.post("/", response_model=CustomerRead)
async def create_customer(customer: CustomerCreate, db: AsyncSession = Depends(get_db)):
    new_customer = Customer(**customer.dict())
    db.add(new_customer)
    await db.commit()
    await db.refresh(new_customer)
    return new_customer

@router.get("/{customer_id}", response_model=CustomerRead)
async def get_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Customer).where(Customer.id == customer_id))
    customer = result.scalar_one_or_none()
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
