# models/pickup_request.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .customer import Customer
from .base import Base
from sqlalchemy.sql import func
import enum

class PickupStatus(str, enum.Enum):
    PENDING = "PENDING"
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class PickupRequest(Base):
    __tablename__ = "pickup_requests"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    pickup_location = Column(String, nullable=False)
    pickup_time = Column(DateTime, nullable=False)
    item_description = Column(String, nullable=True)
    status = Column(Enum(PickupStatus), default=PickupStatus.PENDING, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    customer = relationship("Customer", backref="pickup_requests")

    def __repr__(self):
        return f"<PickupRequest {self.id} status={self.status}>"
