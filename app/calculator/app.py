from fastapi import FastAPI, HTTPException
import logging

from app.operation.arithmetic import Add, Subtract, Multiply, Divide

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI(title="Calculator API")

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