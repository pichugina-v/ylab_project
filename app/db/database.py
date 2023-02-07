import os
from collections.abc import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

engine = create_async_engine(os.getenv('POSTGRES_URL'), echo=True)
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
