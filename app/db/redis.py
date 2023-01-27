import os
from dotenv import load_dotenv

import redis

load_dotenv()


pool = redis.ConnectionPool(
    host=f'{os.getenv("REDIS_HOST")}',
    port=os.getenv('REDIS_PORT'),
    db=os.getenv('REDIS_DB')
)

def get_redis():
    return redis.Redis(connection_pool=pool)
