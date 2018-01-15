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
from dice.utils import to_int
from pyparsing import (
    CaselessLiteral, Forward, Literal, OneOrMore, StringStart, StringEnd,
    Suppress, Word, nums, opAssoc)
import logging
import re

#: The module logger.
logger = logging.getLogger(__name__)


class TokenParser(object):
    pass


class DiceParser(TokenParser):
    """
    Parser that returns the ``rolls`` and ``sides`` from the first dice term
    in a passed string.
    """

    def high(self, string):
        pass

    def low(self, string):
        pass

    def match(self, subject):
        """
        Return the first dice term literal from the given ``subject``.

        If no dice term literal exists in the ``subject`` raise a
        ``ValueError``.

        :param subject: the string with the dice term literal.
        :type subject: str
        :return: the first dice term literal.
        :rtype str:
        """
        logger.debug(str.format("Deriving dice term literal from string: {0}", subject))
        regex = re.compile(self.pattern, re.VERBOSE)
        match = regex.match(subject)

        #: If the regular expression cannot find a match for the subject
        #: we should throw a ValueError because the passed string is not
        #: a valid dice term literal.
        if match is None:
            raise ValueError(str.format("Invalid dice term literal: {0}", subject))
        return str(match.group("term"))

    def mean(self, string):
        pass

    def parse(self, string):
        """
        Parse and return a ``Dice`` token from the given ``string``.

        This method is strict in its interpretation, expecting a dice roll
        term and nothing else. If operands and other terms are passed to this
        method, they will be dropped. E.g.::

          1d6             -> Dice<rolls=1, sides=6>
          1d6+1           -> Dice<rolls=1, sides=6>
          1d6!reroll(1,2) -> Dice<rolls=1, sides=6>

        :param cls: the class
        :param string: the dice roll term, e.g. ``1d6``
        """
        string = self.trim(string)
        rolls, sides = string.split('d', 1)
        return string, to_int(rolls, 1), to_int(sides, 1)

    @property
    def pattern(self):
        """
        Return regular expression pattern that selects the first valid dice
        roll term in a string sequence.
        """
        pattern = (
            r"^.*?"                        #: Skip characters (non-greedy)
            r"(?P<term>\d*[dD][\dF]+){1}"  #: Matches the first proper
                                            #: dice term pattern
            r".*?$"                         #: Skip characters (non-greedy)
        )
        return pattern

    def trim(self, string):
        return self.match(string)


class ExpressionParser(TokenParser):

    def grammar(self):
        pass

    def parse(self, string):
        # An integer value
        integer = Word(nums)
        integer.setParseAction(Integer.parse)
        integer.setName("integer")

        # An expression in dice notation
        expression = StringStart() + operatorPrecedence(integer, [
            (CaselessLiteral('d').suppress(), 2, opAssoc.LEFT, Dice.parse_binary),
            (CaselessLiteral('d').suppress(), 1, opAssoc.RIGHT, Dice.parse_unary),

            (Literal('/').suppress(), 2, opAssoc.LEFT, Div.parse),
            (Literal('*').suppress(), 2, opAssoc.LEFT, Mul.parse),
            (Literal('-').suppress(), 2, opAssoc.LEFT, Sub.parse),
            (Literal('+').suppress(), 2, opAssoc.LEFT, Add.parse),

            (CaselessLiteral('t').suppress(), 1, opAssoc.LEFT, Total.parse),
            (CaselessLiteral('s').suppress(), 1, opAssoc.LEFT, Sort.parse),

            (Literal('^').suppress(), 2, opAssoc.LEFT, Keep.parse),
            (Literal('v').suppress(), 2, opAssoc.LEFT, Drop.parse),
        ]) + StringEnd()
        expression.setName("expression")
