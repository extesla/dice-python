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
from dice.grammar import term
from dice.tokens import Dice
from pprint import pprint
from pyparsing import ParseException
import pytest


def test_term_dice_only():
    parse_result = term().parseString("1d6")
    tokens = parse_result.asList()
    assert len(tokens) == 1

    actual = tokens.pop()
    expected = Dice(rolls=1, sides=6)
    assert actual == expected


def test_term_dice_only_invalid():
    token = term()
    with pytest.raises(ParseException):
        token.parseString("1d1.2")
    with pytest.raises(ParseException):
        token.parseString("1d-6")
    with pytest.raises(ParseException):
        token.parseString("1t6")


def test_term_dice_only_uppercase():
    #NOTE:  this is the same as in test_term_dice_only as CaselessLiteral will
    # return the case of the defined matchString, not the search string passed
    # into parse.   -ZR
    parse_result = term().parseString("1D6")
    tokens = parse_result.asList()
    assert len(tokens) == 1

    actual = tokens.pop()
    expected = Dice(rolls=1, sides=6)
    assert actual == expected


def test_term_dice_with_flag():
    parse_result = term().parseString("1d6!keep")
    tokens = parse_result.asList()
    assert len(tokens) == 1

    actual = tokens.pop()
    expected = [Dice(rolls=1, sides=6), "!keep"]
    assert len(actual) == 2
    assert actual == expected


def test_term_dice_with_operator():
    parse_result = term().parseString("1d6+5")
    tokens = parse_result.asList()
    assert len(tokens) == 1

    actual = tokens.pop()
    expected = [Dice(rolls=1, sides=6), "+", 5]
    assert len(actual) == 3
    assert actual == expected


def test_term_dice_with_flag_and_operator():
    parse_result = term().parseString("1d6!keep+5")
    tokens = parse_result.asList()
    assert len(tokens) == 1

    actual = tokens.pop()
    expected = [[Dice(rolls=1, sides=6), "!keep"], "+", 5]
    assert len(actual) == 3
    assert actual == expected


def test_term_dice_with_flag_and_operator_uppercase():
    parse_result = term().parseString("1D6!KEEP+5")
    tokens = parse_result.asList()
    assert len(tokens) == 1

    actual = tokens.pop()
    expected = [[Dice(rolls=1, sides=6), "!keep"], "+", 5]
    assert len(actual) == 3
    assert len(actual[0]) == 2
    assert actual == expected


def test_term_dice_with_flag_and_operator_invalid():
    token = term()
    with pytest.raises(ParseException):
        token.parseString("1d6!keeper+5")
    with pytest.raises(ParseException):
        token.parseString("1d6a!keep+5")
    with pytest.raises(ParseException):
        token.parseString("1d6!advant+5")
