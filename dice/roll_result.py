from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from dice.execution.result import ExecutionResult


@dataclass
class RollResult:
    """Combined result of execution and optional evaluation."""

    execution: ExecutionResult
    evaluation: dict[str, Any] | None = None

    @property
    def total(self) -> int | float:
        return self.execution.total

    @property
    def tree(self) -> dict[str, Any]:
        return self.execution.tree

    @property
    def expression(self) -> str:
        return self.execution.expression
