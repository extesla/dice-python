import logging

from dice.tokens import Dice
from pyparsing import CaselessLiteral, Optional

from dice.grammar.dice_sides import dice_sides
from dice.grammar.integer import integer

logger = logging.getLogger(__name__)


def dice():
    """
    Return the Backus-Naur form (BNF) of the dice grammar.

    :return: The BNF grammar for dice roll notation, e.g. 1d6.
    """

    def transformer(string, location, tokens):
        logger.debug(
            (
                "Transforming parsed text: `{}` into Dice token with "
                "the following parts: {}"
            ).format(string, str(tokens))
        )
        return Dice(rolls=tokens["dice_rolls"], sides=tokens["dice_sides"])

    #: Create the sub-symbols (rolls and sides) for the dice grammar.
    rolls = Optional(integer(), default=1).setResultsName("dice_rolls")
    sides = dice_sides().setResultsName("dice_sides")

    symbol = rolls + CaselessLiteral("d") + sides
    symbol.setName("dice")
    symbol.setParseAction(transformer)
    return symbol
