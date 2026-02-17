from __future__ import annotations

from app.operation import Add, Divide, Multiply, Subtract
from app.operation.base import Operation

from .calculation import Calculation


class CalculationFactory:
    _ops: dict[str, type[Operation]] = {
        "add": Add,
        "+": Add,
        "subtract": Subtract,
        "-": Subtract,
        "multiply": Multiply,
        "*": Multiply,
        "divide": Divide,
        "/": Divide,
    }

    @classmethod
    def create(cls, op_token: str, a: float, b: float) -> Calculation:
        token = op_token.strip().lower()

        # LBYL: check before you leap
        if token not in cls._ops:
            raise ValueError(f"Unknown operation: {op_token}")

        operation = cls._ops[token]()
        return Calculation.create(operation, a, b)

    @classmethod
    def supported_operations(cls) -> list[str]:
        return ["add", "subtract", "multiply", "divide"]