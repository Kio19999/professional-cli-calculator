from app.schemas import CalculationCreate
from app.crud import compute_result

def test_compute_add():
    calc = CalculationCreate(a=2, b=3, type="add")
    assert compute_result(calc) == 5

def test_compute_subtract():
    calc = CalculationCreate(a=10, b=4, type="subtract")
    assert compute_result(calc) == 6

def test_compute_multiply():
    calc = CalculationCreate(a=3, b=5, type="multiply")
    assert compute_result(calc) == 15

def test_compute_divide():
    calc = CalculationCreate(a=8, b=2, type="divide")
    assert compute_result(calc) == 4