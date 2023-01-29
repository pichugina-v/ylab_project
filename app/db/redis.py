import os

import redis
from dotenv import load_dotenv

load_dotenv()


def create_redis():
    redis.ConnectionPool(
        host=f'{os.getenv("REDIS_HOST")}',
        port=os.getenv('REDIS_PORT'),
        db=os.getenv('REDIS_DB'),
    )


pool = create_redis()


def get_redis():
    return redis.Redis(connection_pool=pool)
