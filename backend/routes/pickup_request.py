# routes/pickup_request.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from ..config import settings
from ..models import PickupRequest, PickupStatus, Customer
from ..schemas import PickupRequestCreate, PickupRequestRead, PickupRequestUpdate
from ..database import get_db
from ..services.assignment import assign_driver

router = APIRouter(prefix="/pickup-requests", tags=["pickup-requests"])

@router.post("/", response_model=PickupRequestRead)
async def create_pickup_request(req: PickupRequestCreate, db: AsyncSession = Depends(get_db)):
    # Verify customer exists
    cust = await db.get(Customer, req.customer_id)
    if not cust:
        raise HTTPException(status_code=404, detail="Customer not found")
    new_req = PickupRequest(**req.dict())
    db.add(new_req)
    await db.commit()
    await db.refresh(new_req)
    # Trigger assignment logic
    await assign_driver(new_req.id, db)
    return new_req

@router.get("/{req_id}", response_model=PickupRequestRead)
async def get_pickup_request(req_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PickupRequest).where(PickupRequest.id == req_id))
    req = result.scalar_one_or_none()
    if not req:
        raise HTTPException(status_code=404, detail="Pickup request not found")
    return req

@router.put("/{req_id}", response_model=PickupRequestRead)
async def update_pickup_request(req_id: int, payload: PickupRequestUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(PickupRequest).where(PickupRequest.id == req_id))
    req = result.scalar_one_or_none()
    if not req:
        raise HTTPException(status_code=404, detail="Pickup request not found")
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(req, key, value)
    await db.commit()
    await db.refresh(req)
    return req
