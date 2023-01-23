import os
from dotenv import load_dotenv

from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from main import app
from app.db.sqlalchemy_base import Base

load_dotenv()

SQLALCHEMY_DATABASE_URL = (f'postgresql://{os.getenv("POSTGRES_USER")}:'
                                f'{os.getenv("POSTGRES_PASSWORD")}@'
                                f'{os.getenv("POSTGRES_SERVICE")}:'
                                f'{os.getenv("POSTGRES_PORT")}/'
                                f'{os.getenv("POSTGRES_DB")}')

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

@fixture(scope='session')
def client():
    client = TestClient(app)
    return client

@fixture(scope='session')
def db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

@fixture(autouse=True, scope="function")
def clear_db(db):
    for tbl in reversed(Base.metadata.sorted_tables):
        db.execute(tbl.delete())
    db.execute("ALTER SEQUENCE menus_id_seq RESTART WITH 1")
    db.execute("ALTER SEQUENCE submenus_id_seq RESTART WITH 1")
    db.execute("ALTER SEQUENCE dishes_id_seq RESTART WITH 1")
    db.commit()
