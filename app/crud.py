from sqlalchemy.orm import Session
from .models import User, Calculation
from .schemas import UserCreate, CalculationCreate, CalculationType
from .security import hash_password, verify_password


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, user: UserCreate):
    if get_user_by_username(db, user.username):
        raise ValueError("Username already exists")

    if get_user_by_email(db, user.email):
        raise ValueError("Email already exists")

    db_user = User(
        username=user.username,
        email=user.email,
        password_hash=hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def verify_user_login(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        raise ValueError("Invalid username or password")

    if not verify_password(password, user.password_hash):
        raise ValueError("Invalid username or password")

    return user


def compute_result(calculation: CalculationCreate) -> float:
    if calculation.type == CalculationType.add:
        return calculation.a + calculation.b

    if calculation.type == CalculationType.subtract:
        return calculation.a - calculation.b

    if calculation.type == CalculationType.multiply:
        return calculation.a * calculation.b

    if calculation.type == CalculationType.divide:
        if calculation.b == 0:
            raise ValueError("Division by zero is not allowed")
        return calculation.a / calculation.b

    if calculation.type == CalculationType.power:
        return calculation.a ** calculation.b

    raise ValueError("Invalid calculation type")


def create_calculation(db: Session, calculation: CalculationCreate):
    result = compute_result(calculation)

    db_calculation = Calculation(
        a=calculation.a,
        b=calculation.b,
        type=calculation.type.value,
        result=result
    )
    db.add(db_calculation)
    db.commit()
    db.refresh(db_calculation)
    return db_calculation


def get_all_calculations(db: Session):
    return db.query(Calculation).all()


def get_calculation_by_id(db: Session, calculation_id: int):
    return db.query(Calculation).filter(Calculation.id == calculation_id).first()


def update_calculation(db: Session, calculation_id: int, calculation):
    db_calculation = get_calculation_by_id(db, calculation_id)
    if not db_calculation:
        raise ValueError("Calculation not found")

    result = compute_result(calculation)

    db_calculation.a = calculation.a
    db_calculation.b = calculation.b
    db_calculation.type = calculation.type.value
    db_calculation.result = result

    db.commit()
    db.refresh(db_calculation)
    return db_calculation


def delete_calculation(db: Session, calculation_id: int):
    db_calculation = get_calculation_by_id(db, calculation_id)
    if not db_calculation:
        raise ValueError("Calculation not found")

    db.delete(db_calculation)
    db.commit()
    return {"message": "Calculation deleted successfully"}