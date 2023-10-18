from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
    AsyncEngine
)
from sqlalchemy.orm import DeclarativeBase

from settings import settings


# Create base model.
class Base(DeclarativeBase):
    ...


# Create async engine.
engine: AsyncEngine = create_async_engine(url=settings.DB_URL)

# Create async session.
session_factory: AsyncSession = async_sessionmaker(engine)
