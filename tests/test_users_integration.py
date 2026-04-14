import os
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base, get_db
from app.calculator.app import app

TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/fastapi_db"
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

def setup_module():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def teardown_module():
    Base.metadata.drop_all(bind=engine)

def test_create_user_success():
    response = client.post("/users", json={
        "username": "user1",
        "email": "user1@example.com",
        "password": "secret123"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == "user1"
    assert "password_hash" not in data

def test_duplicate_username():
    client.post("/users", json={
        "username": "duplicate_user",
        "email": "first@example.com",
        "password": "secret123"
    })

    response = client.post("/users", json={
        "username": "duplicate_user",
        "email": "second@example.com",
        "password": "secret123"
    })
    assert response.status_code == 400

def test_invalid_email():
    response = client.post("/users", json={
        "username": "user2",
        "email": "invalid-email",
        "password": "secret123"
    })
    assert response.status_code == 422