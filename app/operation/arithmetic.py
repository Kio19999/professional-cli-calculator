from __future__ import annotations

from .base import Operation


class Add(Operation):
    name = "add"

    def execute(self, a: float, b: float) -> float:
        return a + b


class Subtract(Operation):
    name = "subtract"

    def execute(self, a: float, b: float) -> float:
        return a - b


class Multiply(Operation):
    name = "multiply"

    def execute(self, a: float, b: float) -> float:
        return a * b


class Divide(Operation):
    name = "divide"

    def execute(self, a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b