"""dice — a Python library for rolling dice with Roll20-compatible notation."""

import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

from dice.constants import SYNTAX_VERSION  # noqa: E402
from dice.errors import DiceError, DiceExecutionError, DiceParseError  # noqa: E402
from dice.evaluation import (  # noqa: E402
    DefaultEvaluator,
    Evaluator,
    evaluate,
    register_evaluator,
)
from dice.execution import ExecutionConfig, ExecutionResult, execute  # noqa: E402
from dice.grammar import ParseResult, parse, validate  # noqa: E402
from dice.rng import RNG, DefaultRNG, SeededRNG  # noqa: E402
from dice.roll_result import RollResult  # noqa: E402
from dice.terms import (  # noqa: E402
    DiceTerm,
    DieResult,
    FateDiceTerm,
    FunctionTerm,
    GroupTerm,
    NumericTerm,
    OperatorTerm,
    ParentheticalTerm,
    RollExpression,
    RollTerm,
)

# Legacy roll function preserved for migration
from dice.roll import roll as roll_legacy  # noqa: E402, F401


def roll(
    expression: str,
    *,
    rng: RNG | None = None,
    config: ExecutionConfig | None = None,
    system: str | None = None,
    template: str | None = None,
    context: dict | None = None,
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


__all__ = [
    # Core API
    "roll",
    "parse",
    "validate",
    "execute",
    "evaluate",
    "register_evaluator",
    # Result types
    "ParseResult",
    "ExecutionResult",
    "ExecutionConfig",
    "RollResult",
    # Evaluator
    "Evaluator",
    "DefaultEvaluator",
    # RNG
    "RNG",
    "DefaultRNG",
    "SeededRNG",
    # Errors
    "DiceError",
    "DiceParseError",
    "DiceExecutionError",
    # Terms
    "RollTerm",
    "RollExpression",
    "DiceTerm",
    "FateDiceTerm",
    "NumericTerm",
    "OperatorTerm",
    "ParentheticalTerm",
    "GroupTerm",
    "FunctionTerm",
    "DieResult",
    # Constants
    "SYNTAX_VERSION",
]
