# database/engine.py
import asyncio
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from ..config import settings

DATABASE_URL = settings.DATABASE_URL

engine: AsyncEngine = create_async_engine(DATABASE_URL, echo=False, future=True)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def get_db() -> AsyncSession:
    async with async_session() as session:
        yield session

# Utility to create tables
async def init_models():
    from ..models import Base
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# For scripts
if __name__ == "__main__":
    asyncio.run(init_models())
