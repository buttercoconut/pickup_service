# Update __init__ to import Base
# models/__init__.py
from .base import Base
from .customer import Customer
from .pickup_request import PickupRequest
from .pickup_driver import PickupDriver
from .pickup_assignment import PickupAssignment

__all__ = [
    "Base",
    "Customer",
    "PickupRequest",
    "PickupDriver",
    "PickupAssignment",
]
