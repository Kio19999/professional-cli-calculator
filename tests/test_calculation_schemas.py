import pytest
from pydantic import ValidationError
from app.schemas import CalculationCreate

def test_calculation_create_valid_add():
    calc = CalculationCreate(a=10, b=5, type="add")
    assert calc.a == 10
    assert calc.b == 5
    assert calc.type.value == "add"

def test_calculation_create_valid_divide():
    calc = CalculationCreate(a=10, b=2, type="divide")
    assert calc.type.value == "divide"

def test_calculation_create_invalid_type():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=5, type="power")

def test_calculation_create_divide_by_zero():
    with pytest.raises(ValidationError):
        CalculationCreate(a=10, b=0, type="divide")