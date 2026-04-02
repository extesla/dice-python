from pyparsing import Group

from dice.grammar.dice import dice
from dice.grammar.flags import flags
from dice.grammar.integer import integer


def operand():
    """
    The Backus-Naur form (BNF) of the grammar defining an ``operand``.

    An operand, in its simplest definition, is any dice or numeric BNF grammar
    that can be operated on.

    :return: The operand BNF.
    """
    token = dice() ^ Group(dice() + flags()) ^ integer()
    token.setName("operand")
    token.setResultsName("operand")
    return token
