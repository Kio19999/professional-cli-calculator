from __future__ import annotations

from dataclasses import dataclass

from app.operation.base import Operation


@dataclass(frozen=True)
class Calculation:
    operation: Operation
    a: float
    b: float
    result: float

    @classmethod
    def create(cls, operation: Operation, a: float, b: float) -> "Calculation":
        result = operation.execute(a, b)
        return cls(operation=operation, a=a, b=b, result=result)

    def __str__(self) -> str:
        return f"{self.operation.name}({self.a}, {self.b}) = {self.result}"