import os

from celery import Celery
from dotenv import load_dotenv

load_dotenv()


celery = Celery(
    'tasks',
    broker=os.getenv('RABBITMQ_URL'),
    backend='rpc://',
    include=['app.v1.celery.tasks'],
)
