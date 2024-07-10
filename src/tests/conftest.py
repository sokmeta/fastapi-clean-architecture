import pytest
from core.config import engine, SessionLocal
from main import app
from fastapi.testclient import TestClient


@pytest.fixture(scope="module")
def db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
        yield c
