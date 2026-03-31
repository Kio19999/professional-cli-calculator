import pytest

from app.calculation import CalculationFactory, CalculationHistory
from app.calculation.calculation import Calculation
from app.operation.arithmetic import Add, Subtract, Multiply, Divide


@pytest.mark.parametrize(
    "token,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("+", 2, 3, 5),
        ("subtract", 10, 4, 6),
        ("-", 10, 4, 6),
        ("multiply", 3, 5, 15),
        ("*", 3, 5, 15),
        ("divide", 8, 2, 4),
        ("/", 8, 2, 4),
    ],
)
def test_factory(token, a, b, expected):
    calc = CalculationFactory.create(token, a, b)
    assert calc.result == expected


def test_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("power", 2, 3)


def test_history():
    history = CalculationHistory()
    assert history.is_empty()

    calc = CalculationFactory.create("add", 1, 2)
    history.add(calc)

    assert not history.is_empty()
    assert len(history.all()) == 1


def test_history_clear():
    history = CalculationHistory()
    calc = CalculationFactory.create("add", 1, 1)
    history.add(calc)
    history.clear()
    assert history.is_empty()


def test_supported_operations():
    ops = CalculationFactory.supported_operations()
    assert "add" in ops
    assert "divide" in ops


def test_calculation_str():
    calc = Calculation.create(Add(), 2, 3)
    s = str(calc)
    assert "add" in s
    assert "= 5" in s


def test_add():
    assert Add().execute(2, 3) == 5


def test_subtract():
    assert Subtract().execute(10, 4) == 6


def test_multiply():
    assert Multiply().execute(3, 5) == 15


def test_divide():
    assert Divide().execute(8, 2) == 4


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        Divide().execute(8, 0)