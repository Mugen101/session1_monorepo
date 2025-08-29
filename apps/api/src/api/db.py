from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlmodel import SQLModel
import os

DATABASE_URL = os.getenv("DATABASE_URL").replace("postgresql+psycopg", "postgresql+psycopg_async")

engine = create_async_engine(DATABASE_URL, pool_size=5, max_overflow=10, pool_timeout=30)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

@asynccontextmanager
async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session
