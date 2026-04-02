from __future__ import annotations

from dataclasses import dataclass, field

from dice.errors import DiceParseError
from dice.terms import RollExpression


@dataclass
class ParseResult:
    ast: RollExpression
    expression: str
    syntax_version: str
    errors: list[DiceParseError] = field(default_factory=list)
