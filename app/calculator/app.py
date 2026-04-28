from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import FileResponse
import logging
import os
from sqlalchemy.orm import Session

from app.operation.arithmetic import Add, Subtract, Multiply, Divide
from app.database import Base, engine, get_db
from app.schemas import (
    UserCreate,
    UserRead,
    UserLogin,
    TokenResponse,
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
from app.security import create_access_token

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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


@app.get("/")
def home():
    return {"message": "Calculator API is running"}


@app.get("/register-page")
def register_page():
    return FileResponse(os.path.join(FRONTEND_DIR, "register.html"))


@app.get("/login-page")
def login_page():
    return FileResponse(os.path.join(FRONTEND_DIR, "login.html"))


@app.post("/register", response_model=UserRead, status_code=201)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return create_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/login", response_model=TokenResponse)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = verify_user_login(db, user.username, user.password)
        token = create_access_token({"sub": db_user.username})
        return {
            "access_token": token,
            "token_type": "bearer"
        }
    except ValueError:
        raise HTTPException(status_code=401, detail="Invalid username or password")


@app.get("/add")
def add_numbers(a: float, b: float):
    result = add_op.execute(a, b)
    return {"operation": "add", "a": a, "b": b, "result": result}


@app.get("/subtract")
def subtract_numbers(a: float, b: float):
    result = subtract_op.execute(a, b)
    return {"operation": "subtract", "a": a, "b": b, "result": result}


@app.get("/multiply")
def multiply_numbers(a: float, b: float):
    result = multiply_op.execute(a, b)
    return {"operation": "multiply", "a": a, "b": b, "result": result}


@app.get("/divide")
def divide_numbers(a: float, b: float):
    try:
        result = divide_op.execute(a, b)
        return {"operation": "divide", "a": a, "b": b, "result": result}
    except ZeroDivisionError as e:
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
def edit_calculation(calculation_id: int, calculation: CalculationUpdate, db: Session = Depends(get_db)):
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


@app.delete("/calculations/{calculation_id}")
def remove_calculation(calculation_id: int, db: Session = Depends(get_db)):
    try:
        return delete_calculation(db, calculation_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@app.get("/calculations-page")
def calculations_page():
    return FileResponse(os.path.join(FRONTEND_DIR, "calculations.html"))