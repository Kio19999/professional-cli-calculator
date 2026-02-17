from __future__ import annotations

from abc import ABC, abstractmethod


class Operation(ABC):
    name: str

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        raise NotImplementedError