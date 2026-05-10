# models/pickup_driver.py
from sqlalchemy import Column, Integer, String
from .base import Base

class PickupDriver(Base):
    __tablename__ = "pickup_drivers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    vehicle_info = Column(String, nullable=True)
    is_available = Column(Integer, default=1)  # 1: available, 0: busy

    def __repr__(self):
        return f"<PickupDriver {self.id} {self.name}>"
