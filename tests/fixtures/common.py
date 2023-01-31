import os
from collections.abc import Generator

from dotenv import load_dotenv
from fastapi.testclient import TestClient
from pytest import fixture
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.db.database import get_db
from app.db.sqlalchemy_base import Base
from main import app

load_dotenv()

SQLALCHEMY_DATABASE_URL = (
    f'postgresql://{os.getenv("TEST_POSTGRES_USER")}:'
    f'{os.getenv("TEST_POSTGRES_PASSWORD")}@'
    f'{os.getenv("TEST_POSTGRES_SERVICE")}/'
    f'{os.getenv("TEST_POSTGRES_DB")}'
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
TestingSessionLocal = sessionmaker(
    bind=engine, autocommit=False, autoflush=False,
)


@fixture
def db() -> Generator:
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@fixture
def client(db) -> TestClient:
    def _get_db_override():
        return db
    app.dependency_overrides[get_db] = _get_db_override
    return TestClient(app)
