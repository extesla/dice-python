import logging

#: Initialize the root level logging...
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

from dice.evaluation import evaluate, register_evaluator  # noqa: E402
from dice.execution import ExecutionConfig, ExecutionResult, execute  # noqa: E402
from dice.grammar import parse, validate  # noqa: E402
from dice.rng import RNG, DefaultRNG, SeededRNG  # noqa: E402
from dice.roll_result import RollResult  # noqa: E402

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
    """Parse, execute, and optionally evaluate a dice expression."""
    parsed = parse(expression)
    if parsed.errors:
        raise parsed.errors[0]
    exec_result = execute(parsed.ast, rng=rng, config=config)
    eval_result = None
    if system is not None or template is not None or context is not None:
        eval_result = evaluate(exec_result.tree, system, template, context)
    return RollResult(execution=exec_result, evaluation=eval_result)
