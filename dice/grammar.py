# The MIT License (MIT)
#
# Copyright (c) 2016 Sean Quinn
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
from dice.operators import Add, Subtract, Divide, Multiply
from dice.tokens import Dice, Expression, Integer
from pyparsing import (
    CaselessLiteral,
    Group,
    Literal,
    OneOrMore,
    Optional,
    StringStart,
    StringEnd,
    Word,
    nums,
    ZeroOrMore,
)
import logging

#: Module logger
logger = logging.getLogger(__name__)


def dice():
    """
    Return the Backus-Naur form (BNF) of the dice grammar.

    :return: The BNF grammar for dice roll notation, e.g. 1d6.
    """
    def transformer(string, location, tokens):
        logger.debug(("Transforming parsed text: `{}` into Dice token with "
            "the following parts: {}").format(string, str(tokens)))
        return Dice(rolls=tokens["dice_rolls"], sides=tokens["dice_sides"])

    #: Create the sub-symbols (rolls and sides) for the dice grammar.
    rolls = Optional(integer(), default=1).setResultsName("dice_rolls")
    sides = dice_sides().setResultsName("dice_sides")

    symbol = (rolls + CaselessLiteral("d") + sides)
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
        integer()
        | CaselessLiteral("fate")
        | CaselessLiteral("f")
        #| StringStart() + CaselessLiteral("f") + StringEnd() \
        #| StringStart() + CaselessLiteral("fate") + StringEnd()
    )
    return token


def expression():
    def transformer(string, location, tokens):
        logger.debug(("Transforming parsed text: `{}` into Expression token "
            "with the following parts: {}").format(string, str(tokens)))
        return Expression(_raw_text=string, tokens=tokens)
    token = Optional(Literal("(")) + term() + Optional(Literal(")"))
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


def operator():
    token = Literal("+") | Literal("-") | Literal("/") | Literal("*")
    token.setName("operator")
    return token


def term():
    """
    """
    token = (
        StringStart() + dice() + StringEnd()
      | StringStart() + dice() + operator() + integer() + StringEnd()
      | StringStart() + dice() + flags() + StringEnd()
      | StringStart() + dice() + flags() + operator() + integer() + StringEnd()
    )
    token.setName("term")
    return token
