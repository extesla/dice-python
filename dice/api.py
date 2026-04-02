from __future__ import annotations

from typing import Any

from dice.evaluation import evaluate
from dice.execution import ExecutionConfig, execute
from dice.grammar import parse
from dice.rng import RNG
from dice.roll_result import RollResult


def roll(
    expression: str,
    *,
    rng: RNG | None = None,
    config: ExecutionConfig | None = None,
    system: str | None = None,
    template: str | None = None,
    context: dict[str, Any] | None = None,
) -> RollResult:
    """Parse, execute, and optionally evaluate a dice expression.

    This is the primary entry point for the library.

    Args:
        expression: A Roll20-compatible dice expression (e.g. "2d20kh1+7").
        rng: Optional RNG instance for deterministic rolling.
        config: Optional ExecutionConfig for safety limits.
        system: Optional system identifier for evaluation (e.g. "dnd35e").
        template: Optional template identifier for evaluation (e.g. "attack").
        context: Optional context dict for evaluation (e.g. {"target_dc": 15}).

    Returns:
        RollResult containing execution tree and optional evaluation.

    Raises:
        DiceParseError: If the expression cannot be parsed.
        DiceExecutionError: If execution fails (safety limits, etc.).
    """
    parsed = parse(expression)
    if parsed.errors:
        raise parsed.errors[0]
    exec_result = execute(parsed.ast, rng=rng, config=config)
    eval_result = None
    if system is not None or template is not None or context is not None:
        eval_result = evaluate(exec_result.tree, system, template, context)
    return RollResult(execution=exec_result, evaluation=eval_result)
