from pyparsing import CaselessLiteral

from dice.grammar.integer import integer


def dice_sides():
    """
    Return the Backus-Naur form (BNF) of the grammar describing the number of
    sides for a die.

    :return: The BNF grammar for the number of sides of a dice, e.g. 6.
    """
    token = (
        integer()
        | CaselessLiteral("fate")
        | CaselessLiteral("f")
    )
    return token
