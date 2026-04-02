from __future__ import annotations

from dataclasses import dataclass

from dice.constants import MAX_DICE_COUNT, MAX_EXPRESSION_DEPTH, MAX_EXPLOSIONS


@dataclass
class ExecutionConfig:
    """Safety limits and execution options."""

    max_dice: int = MAX_DICE_COUNT
    max_depth: int = MAX_EXPRESSION_DEPTH
    max_explosions: int = MAX_EXPLOSIONS
