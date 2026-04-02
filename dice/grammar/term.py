from pyparsing import Group, StringStart, StringEnd

from dice.grammar.operand import operand
from dice.grammar.operator import operator


def term():
    token = (
        StringStart() + operand() + StringEnd()
        ^ StringStart() + Group(operand() + operator() + operand()) + StringEnd()
    )
    token.setName("term")
    return token
