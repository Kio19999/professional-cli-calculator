import pytest

from app.operation import Add, Subtract, Multiply, Divide


@pytest.mark.parametrize(
    "op,a,b,expected",
    [
        (Add(), 2, 3, 5),
        (Subtract(), 10, 4, 6),
        (Multiply(), 3, 5, 15),
        (Divide(), 8, 2, 4),
        (Add(), -1, 1, 0),
        (Multiply(), 2.5, 2, 5.0),
    ],
)
def test_operations_execute(op, a, b, expected):
    assert op.execute(a, b) == expected


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Divide().execute(10, 0)


from app.operation.base import Operation


class DummyOperation(Operation):
    name = "dummy"

    def execute(self, a, b):
        return a


def test_operation_base_not_implemented():
    with pytest.raises(TypeError):
        Operation()  # abstract class cannot be instantiated


def test_dummy_operation():
    op = DummyOperation()
    assert op.execute(5, 10) == 5


from app.operation.base import Operation


class IncompleteOperation(Operation):
    name = "incomplete"

    def execute(self, a: float, b: float) -> float:
        return super().execute(a, b)  # triggers NotImplementedError


def test_operation_execute_not_implemented():
    op = IncompleteOperation()
    with pytest.raises(NotImplementedError):
        op.execute(1, 2)