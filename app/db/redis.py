import os

from dotenv import load_dotenv
from redis import asyncio

load_dotenv()


pool = asyncio.ConnectionPool(
    host=f'{os.getenv("REDIS_SERVICE")}',
    port=os.getenv('REDIS_PORT'),
    db=os.getenv('REDIS_DB'),
)


async def get_redis():
    asynco_redis = await asyncio.Redis(connection_pool=pool)
    try:
        yield asynco_redis
    finally:
        await asynco_redis.close()
