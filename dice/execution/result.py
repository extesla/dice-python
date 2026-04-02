from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ExecutionResult:
    """The output of executing a parsed AST."""

    tree: dict[str, Any]
    total: int | float
    expression: str
    syntax_version: str
