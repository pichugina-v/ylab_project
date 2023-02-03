import os
from collections.abc import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f'postgresql+asyncpg://{os.getenv("POSTGRES_USER")}:'
    f'{os.getenv("POSTGRES_PASSWORD")}@'
    # f'{os.getenv("POSTGRES_HOST")}:'
    f'{os.getenv("POSTGRES_SERVICE")}/'
    f'{os.getenv("POSTGRES_DB")}'
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)
async_session_maker = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_db() -> AsyncGenerator:
    async with async_session_maker() as db:
        try:
            yield db
        finally:
            await db.close()
