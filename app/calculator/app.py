from fastapi import FastAPI, HTTPException, Depends
import logging
from sqlalchemy.orm import Session

from app.operation.arithmetic import Add, Subtract, Multiply, Divide
from app.database import Base, engine, get_db
from app.schemas import (
    UserCreate,
    UserRead,
    UserLogin,
    CalculationCreate,
    CalculationRead,
    CalculationUpdate,
)
from app.crud import (
    create_user,
    verify_user_login,
    create_calculation,
    get_all_calculations,
    get_calculation_by_id,
    update_calculation,
    delete_calculation,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Calculator API")
Base.metadata.create_all(bind=engine)

add_op = Add()
subtract_op = Subtract()
multiply_op = Multiply()
divide_op = Divide()


@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message": "Calculator API is running"}


@app.get("/add")
def add_numbers(a: float, b: float):
    logger.info(f"Add called with a={a}, b={b}")
    result = add_op.execute(a, b)
    logger.info(f"Add result={result}")
    return {"operation": "add", "a": a, "b": b, "result": result}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    logger.info(f"Subtract called with a={a}, b={b}")
    result = subtract_op.execute(a, b)
    logger.info(f"Subtract result={result}")
    return {"operation": "subtract", "a": a, "b": b, "result": result}


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    logger.info(f"Multiply called with a={a}, b={b}")
    result = multiply_op.execute(a, b)
    logger.info(f"Multiply result={result}")
    return {"operation": "multiply", "a": a, "b": b, "result": result}


@app.get("/divide")
def divide_numbers(a: float, b: float):
    logger.info(f"Divide called with a={a}, b={b}")
    try:
        result = divide_op.execute(a, b)
        logger.info(f"Divide result={result}")
        return {"operation": "divide", "a": a, "b": b, "result": result}
    except ZeroDivisionError as e:
        logger.error(str(e))
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/users/register", response_model=UserRead, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/users/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = verify_user_login(db, user.username, user.password)
        return {
            "message": "Login successful",
            "username": db_user.username,
            "email": db_user.email
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/calculations", response_model=CalculationRead, status_code=201)
def add_calculation(calculation: CalculationCreate, db: Session = Depends(get_db)):
    try:
        return create_calculation(db, calculation)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/calculations", response_model=list[CalculationRead])
def browse_calculations(db: Session = Depends(get_db)):
    return get_all_calculations(db)


@app.get("/calculations/{calculation_id}", response_model=CalculationRead)
def read_calculation(calculation_id: int, db: Session = Depends(get_db)):
    calculation = get_calculation_by_id(db, calculation_id)
    if not calculation:
        raise HTTPException(status_code=404, detail="Calculation not found")
    return calculation


@app.put("/calculations/{calculation_id}", response_model=CalculationRead)
def edit_calculation(
    calculation_id: int,
    calculation: CalculationUpdate,
    db: Session = Depends(get_db)
):
    try:
        return update_calculation(db, calculation_id, calculation)
    except ValueError as e:
        if str(e) == "Calculation not found":
            raise HTTPException(status_code=404, detail=str(e))
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/calculations/{calculation_id}")
def remove_calculation(calculation_id: int, db: Session = Depends(get_db)):
    try:
        return delete_calculation(db, calculation_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))