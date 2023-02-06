import asyncio
import os
from collections.abc import AsyncGenerator, Generator

from dotenv import load_dotenv
from httpx import AsyncClient
from pytest_asyncio import fixture
from redis import asyncio as redis_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import get_db
from app.db.redis import get_redis
from app.db.sqlalchemy_base import Base
from main import app

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{os.getenv("TEST_POSTGRES_USER")}:'
    f'{os.getenv("TEST_POSTGRES_PASSWORD")}@'
    f'{os.getenv("TEST_POSTGRES_SERVICE")}/'
    f'{os.getenv("TEST_POSTGRES_DB")}'
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_testing_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@fixture(scope='session')
def event_loop() -> Generator:
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@fixture
async def db() -> AsyncGenerator:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    async with async_testing_session() as db:
        try:
            yield db
        finally:
            await db.close()


@fixture
async def client(db) -> AsyncClient:
    def _get_db_override():
        return db

    app.dependency_overrides[get_db] = _get_db_override
    async with AsyncClient(app=app, base_url='http://test') as client:
        yield client


@fixture()
async def redis_pool() -> AsyncGenerator:
    pool = redis_asyncio.ConnectionPool(
        host=f'{os.getenv("TEST_REDIS_SERVICE")}',
        port=os.getenv('REDIS_PORT'),
        db=os.getenv('TEST_REDIS_DB'),
    )
    asynco_redis = await redis_asyncio.Redis(connection_pool=pool)
    try:
        yield asynco_redis
    finally:
        await asynco_redis.close()


@fixture()
def cache(redis_pool):
    def _get_redis_override():
        return redis_pool

    app.dependency_overrides[get_redis] = _get_redis_override
