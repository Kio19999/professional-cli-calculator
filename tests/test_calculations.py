import pytest

from app.calculation import CalculationFactory, CalculationHistory
from app.calculator.app import parse_number


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


def test_parse_number():
    assert parse_number("10") == 10.0

    with pytest.raises(ValueError):
        parse_number("abc")


from app.calculation.calculation import Calculation
from app.operation.arithmetic import Add
from app.calculator.app import format_help


def test_calculation_str():
    from app.operation.arithmetic import Add
    from app.calculation.calculation import Calculation

    calc = Calculation.create(Add(), 2, 3)
    s = str(calc)
    assert "add" in s
    assert "= 5" in s


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


def test_format_help():
    help_text = format_help()
    assert "help" in help_text
    assert "history" in help_text
    assert "exit" in help_text


import builtins
import pytest

from app.calculator import app as calculator_app


def run_repl_with_inputs(inputs, capsys):
    it = iter(inputs)

    def fake_input(_prompt=""):
        return next(it)

    # patch input()
    original_input = builtins.input
    builtins.input = fake_input
    try:
        calculator_app.repl()
    finally:
        builtins.input = original_input

    return capsys.readouterr().out


def test_repl_help_then_exit(capsys):
    out = run_repl_with_inputs(["help", "exit"], capsys)
    assert "Professional CLI Calculator" in out
    assert "Commands:" in out
    assert "Bye!" in out


def test_repl_history_empty_then_exit(capsys):
    out = run_repl_with_inputs(["history", "exit"], capsys)
    assert "No history yet." in out


def test_repl_add_then_history_then_exit(capsys):
    out = run_repl_with_inputs(
        [
            "add",
            "2",
            "3",
            "history",
            "exit",
        ],
        capsys,
    )
    assert "Result:" in out
    assert "add" in out  # appears in history line


def test_repl_invalid_number(capsys):
    out = run_repl_with_inputs(
        [
            "add",
            "abc",
            "3",
            "exit",
        ],
        capsys,
    )
    assert "Error:" in out
    assert "Invalid number" in out


def test_repl_divide_by_zero(capsys):
    out = run_repl_with_inputs(
        [
            "divide",
            "5",
            "0",
            "exit",
        ],
        capsys,
    )
    assert "Error:" in out
    assert "divide by zero" in out.lower() or "cannot divide by zero" in out.lower()