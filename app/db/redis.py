import os

import redis
from dotenv import load_dotenv

load_dotenv()


def create_redis():
    redis_conn = redis.ConnectionPool(
        host=f'{os.getenv("REDIS_SERVICE")}',
        port=os.getenv('REDIS_PORT'),
        db=os.getenv('REDIS_DB'),
    )
    return redis_conn


pool = create_redis()


def get_redis():
    return redis.Redis(connection_pool=pool)
