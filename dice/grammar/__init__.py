from dice.grammar.parse_result import ParseResult
from dice.grammar.parser import parse, validate

# Legacy grammar function exports
from dice.grammar.dice import dice  # noqa: F401
from dice.grammar.dice_sides import dice_sides  # noqa: F401
from dice.grammar.expression import expression  # noqa: F401
from dice.grammar.flags import flags  # noqa: F401
from dice.grammar.integer import integer  # noqa: F401
from dice.grammar.operand import operand  # noqa: F401
from dice.grammar.operator import operator  # noqa: F401
from dice.grammar.term import term  # noqa: F401

__all__ = [
    # New API
    "ParseResult",
    "parse",
    "validate",
    # Legacy
    "dice",
    "dice_sides",
    "expression",
    "flags",
    "integer",
    "operand",
    "operator",
    "term",
]
