# models/pickup_assignment.py
from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base import Base
from .pickup_driver import PickupDriver
from .pickup_request import PickupRequest, PickupStatus
import enum

class AssignmentStatus(str, enum.Enum):
    ASSIGNED = "ASSIGNED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class PickupAssignment(Base):
    __tablename__ = "pickup_assignments"
    id = Column(Integer, primary_key=True, index=True)
    pickup_request_id = Column(Integer, ForeignKey("pickup_requests.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("pickup_drivers.id"), nullable=False)
    status = Column(Enum(AssignmentStatus), default=AssignmentStatus.ASSIGNED, nullable=False)

    pickup_request = relationship("PickupRequest", backref="assignments")
    driver = relationship("PickupDriver", backref="assignments")

    def __repr__(self):
        return f"<PickupAssignment {self.id} driver={self.driver_id} status={self.status}>"
