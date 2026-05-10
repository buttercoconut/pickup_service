# routes/pickup_driver.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..config import settings
from ..models import PickupDriver
from ..schemas import PickupDriverCreate, PickupDriverRead
from ..database import get_db

router = APIRouter(prefix="/drivers", tags=["drivers"])

@router.post("/", response_model=PickupDriverRead)
async def create_driver(driver: PickupDriverCreate, db: AsyncSession = Depends(get_db)):
    new_driver = PickupDriver(**driver.dict())
    db.add(new_driver)
    await db.commit()
    await db.refresh(new_driver)
    return new_driver

@router.get("/{driver_id}", response_model=PickupDriverRead)
async def get_driver(driver_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PickupDriver).where(PickupDriver.id == driver_id))
    driver = result.scalar_one_or_none()
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver
