# schemas/__init__.py
from .customer import CustomerCreate, CustomerRead
from .pickup_request import PickupRequestCreate, PickupRequestRead, PickupRequestUpdate
from .pickup_driver import PickupDriverCreate, PickupDriverRead

__all__ = [
    "CustomerCreate",
    "CustomerRead",
    "PickupRequestCreate",
    "PickupRequestRead",
    "PickupRequestUpdate",
    "PickupDriverCreate",
    "PickupDriverRead",
]
