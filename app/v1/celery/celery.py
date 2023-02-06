import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()

BROKER_URL = (
    f'amqp://{os.getenv("RABBITMQ_USER")}:'
    f'{os.getenv("RABBITMQ_PASSWORD")}@'
    f'{os.getenv("RABBITMQ_SERVICE")}:'
    f'{os.getenv("RABBITMQ_PORT")}/'
    f'{os.getenv("RABBITMQ_VHOST")}'
)


celery = Celery(
    'tasks',
    broker=BROKER_URL,
    backend='rpc://',
    include=['app.v1.celery.tasks'],
)
