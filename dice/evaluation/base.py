from __future__ import annotations

from typing import Any, Protocol


class Evaluator(Protocol):
    """Protocol for game-system evaluators."""

    def evaluate(
        self,
        execution_tree: dict[str, Any],
        template: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Interpret an execution tree through game-system rules.

        Args:
            execution_tree: The execution tree dict from the executor.
            template: Optional template identifier (e.g. "attack", "save").
            context: Optional structured context (e.g. target DC, skill modifier).

        Returns:
            A dict containing at minimum:
            - primary_total (int | float): the main numeric result
            - outcome (str | None): semantic result ("success", "failure", etc.)
        """
        ...
