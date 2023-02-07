import os

from dotenv import load_dotenv
from redis import asyncio

load_dotenv()


pool = asyncio.ConnectionPool.from_url(str(os.getenv('REDIS_URL')))


async def get_redis():
    asynco_redis = await asyncio.Redis(connection_pool=pool)
    try:
        yield asynco_redis
    finally:
        await asynco_redis.close()
