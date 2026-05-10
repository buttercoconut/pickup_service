# database/session.py
from .engine import async_session

# Expose session factory for external use
SessionLocal = async_session
