# routes/__init__.py
from .customer import router as customer_router
from .pickup_request import router as pickup_request_router
from .pickup_driver import router as pickup_driver_router

__all__ = [
    "customer_router",
    "pickup_request_router",
    "pickup_driver_router",
]
