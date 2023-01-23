import os
from dotenv import load_dotenv
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

SQLALCHEMY_DATABASE_URL = (f'postgresql://{os.getenv("POSTGRES_USER")}:'
                           f'{os.getenv("POSTGRES_PASSWORD")}@'
                           f'{os.getenv("POSTGRES_SERVICE")}:'
                           f'{os.getenv("POSTGRES_PORT")}/'
                           f'{os.getenv("POSTGRES_DB")}')

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 
