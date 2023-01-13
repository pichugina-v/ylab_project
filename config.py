import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = (f'postgresql://{os.getenv("POSTGRES_USER")}:'
                           f'{os.getenv("POSTGRES_PASSWORD")}@'
                           f'{os.getenv("POSTGRES_HOST")}:'
                           f'{os.getenv("POSTGRES_PORT")}/'
                           f'{os.getenv("POSTGRES_DB")}')
