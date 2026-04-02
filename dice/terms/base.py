from __future__ import annotations

import uuid
from abc import ABC, abstractmethod
from typing import Any

from dice.rng import RNG


class RollTerm(ABC):
    """Base class for all roll terms in the AST and execution tree."""

    kind: str  # overridden by each subclass as a class variable

    def __init__(self, *, id: str | None = None) -> None:
        self.id = id or self._generate_id()
        self._evaluated = False

    @abstractmethod
    def evaluate(self, rng: RNG) -> RollTerm:
        """Evaluate this term, populating result data. Returns self."""
        ...

    @abstractmethod
    def to_dict(self) -> dict[str, Any]:
        """Serialize to execution tree dict."""
        ...

    @property
    @abstractmethod
    def total(self) -> int | float:
        """The computed numeric value of this term."""
        ...

    @staticmethod
    def _generate_id() -> str:
        return uuid.uuid4().hex[:8]
