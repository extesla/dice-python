import logging

from pyparsing import (
    CaselessLiteral,
    Group,
    Literal,
    OneOrMore,
    Optional,
    StringEnd,
    StringStart,
    Word,
    ZeroOrMore,
    nums,
)

from dice.operators import Add, Divide, Multiply, Subtract
from dice.tokens import Dice, Expression, Integer

#: Module logger
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


def dice_sides():
    """
    Return the Backus-Naur form (BNF) of the grammar describing the number of
    sides for a die.

    :return: The BNF grammar for the number of sides of a dice, e.g. 6.
    """
    token = (
        integer() | CaselessLiteral("fate") | CaselessLiteral("f")
        # | StringStart() + CaselessLiteral("f") + StringEnd() \
        # | StringStart() + CaselessLiteral("fate") + StringEnd()
    )
    return token


def expression():
    """ """

    def transformer(string, location, tokens):
        return tokens.asList()

    token = OneOrMore(term())
    token.setName("expression")
    token.setParseAction(transformer)
    return token


def flags():
    token = (
        CaselessLiteral("!advantage")
        | CaselessLiteral("!adv")
        | CaselessLiteral("!disadvantage")
        | CaselessLiteral("!dis")
        | CaselessLiteral("!drop")
        | CaselessLiteral("!grow")
        | CaselessLiteral("!keep")
        | CaselessLiteral("!shrink")
        | CaselessLiteral("!take")
    )

    token.setName("flags")
    token.setResultsName("flags")
    return token


def integer():
    token = Word(nums)
    token.setParseAction(Integer.parse)
    token.setName("integer")
    return token


def operand():
    """
    The Backus-Naur form (BNF) of the grammar defining an ``operand``.

    An operand, in its simplest definition, is any dice or numeric BNF grammar
    that can be operated on.

    :return: The operand BNF.
    """
    token = dice() ^ Group(dice() + flags()) ^ integer()
    # token = (Group(dice() + Optional(flags()))) | integer()
    token.setName("operand")
    token.setResultsName("operand")
    return token


def operator():
    token = Literal("+") | Literal("-") | Literal("/") | Literal("*")
    token.setName("operator")
    return token


def term():
    """ """
    token = (
        StringStart() + operand() + StringEnd()
        ^ StringStart() + Group(operand() + operator() + operand()) + StringEnd()
    )
    token.setName("term")
    return token
