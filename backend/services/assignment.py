# services/assignment.py
"""Simple assignment logic: pick the first available driver.
In a real system this would involve geospatial queries and a message queue.
"""
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models import PickupDriver, PickupRequest, PickupAssignment, AssignmentStatus

async def assign_driver(pickup_request_id: int, db: AsyncSession):
    # Find an available driver
    result = await db.execute(select(PickupDriver).where(PickupDriver.is_available == 1))
    driver = result.scalars().first()
    if not driver:
        # No driver available; leave request pending
        return
    # Mark driver as busy
    driver.is_available = 0
    # Create assignment
    assignment = PickupAssignment(
        pickup_request_id=pickup_request_id,
        driver_id=driver.id,
        status=AssignmentStatus.ASSIGNED,
    )
    db.add(assignment)
    # Update request status
    req_result = await db.execute(select(PickupRequest).where(PickupRequest.id == pickup_request_id))
    req = req_result.scalar_one()
    req.status = "ASSIGNED"
    await db.commit()
    await db.refresh(assignment)
    return assignment
