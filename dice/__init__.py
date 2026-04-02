import logging

#: Initialize the root level logging...
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger(__name__)

from dice.execution import ExecutionConfig, ExecutionResult, execute  # noqa: E402
from dice.grammar import parse, validate  # noqa: E402
from dice.rng import RNG, DefaultRNG, SeededRNG  # noqa: E402

# Legacy roll function preserved for migration
from dice.roll import roll as roll_legacy  # noqa: E402, F401


def roll(
    expression: str,
    *,
    rng: RNG | None = None,
    config: ExecutionConfig | None = None,
) -> ExecutionResult:
    """Parse and execute a dice expression. One-call convenience API."""
    parsed = parse(expression)
    if parsed.errors:
        raise parsed.errors[0]
    return execute(parsed.ast, rng=rng, config=config)
