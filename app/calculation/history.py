from __future__ import annotations

from dataclasses import dataclass, field

from .calculation import Calculation


@dataclass
class CalculationHistory:
    _items: list[Calculation] = field(default_factory=list)

    def add(self, calc: Calculation) -> None:
        self._items.append(calc)

    def all(self) -> list[Calculation]:
        return list(self._items)

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def clear(self) -> None:
        self._items.clear()