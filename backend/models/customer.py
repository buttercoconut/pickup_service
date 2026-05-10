# Update models to import Base from base.py
# models/customer.py
from sqlalchemy import Column, Integer, String
from .base import Base

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)

    def __repr__(self):
        return f"<Customer {self.id} {self.name}>"
