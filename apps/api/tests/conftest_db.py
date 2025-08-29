import os
import pytest
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql+psycopg_async://tg:tgpass@localhost:5432/travelg3n_test")
engine = create_async_engine(TEST_DATABASE_URL, pool_size=5, max_overflow=10, pool_timeout=30)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

@pytest.fixture(scope="session", autouse=True)
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)

@pytest.fixture()
async def db_session():
    async with engine.begin() as conn:
        async with SessionLocal() as session:
            trans = await conn.begin()
            yield session
            await trans.rollback()
