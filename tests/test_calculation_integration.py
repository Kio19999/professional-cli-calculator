import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database import Base
from app.crud import create_calculation
from app.schemas import CalculationCreate

TEST_DATABASE_URL = os.getenv(
    "TEST_DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/fastapi_db"
)

engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def setup_module():
    Base.metadata.create_all(bind=engine)

def teardown_module():
    Base.metadata.drop_all(bind=engine)

def test_insert_calculation_record():
    db = TestingSessionLocal()
    calc = CalculationCreate(a=10, b=5, type="add")
    saved = create_calculation(db, calc)

    assert saved.id is not None
    assert saved.a == 10
    assert saved.b == 5
    assert saved.type == "add"
    assert saved.result == 15

    db.close()