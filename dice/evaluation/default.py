from __future__ import annotations

from typing import Any


class DefaultEvaluator:
    """System-agnostic evaluator that extracts totals without interpretation."""

    def evaluate(
        self,
        execution_tree: dict[str, Any],
        template: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        return {
            "primary_total": execution_tree.get("total", 0),
            "outcome": None,
        }
