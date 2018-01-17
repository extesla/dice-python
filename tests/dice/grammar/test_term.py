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
    token = term()
    actual = token.parseString("1d6")
    expected = Dice(rolls=1, sides=6)

    assert len(actual) == 1
    assert actual[0] == expected


def test_term_dice_only_invalid():
    token = term()
    with pytest.raises(ParseException):
        token.parseString("1d1.2")
    with pytest.raises(ParseException):
        token.parseString("1d-6")
    with pytest.raises(ParseException):
        token.parseString("1t6")


def test_term_dice_only_uppercase():
    token = term()
    actual = token.parseString("1D6")
    expected = Dice(rolls=1, sides=6)

    assert len(actual) == 1
    #NOTE:  this is the same as in test_term_dice_only as CaselessLiteral will
    # return the case of the defined matchString, not the search string passed
    # into parse.   -ZR
    assert actual[0] == expected


def test_term_dice_with_flag():
    token = term()
    actual = token.parseString("1d6!keep")
    expected_dice = Dice(rolls=1, sides=6)
    expected_flag = "!keep"

    assert len(actual) == 2
    assert actual[0] == expected_dice
    assert actual[1] == expected_flag


def test_term_dice_with_operator():
    token = term()
    actual = token.parseString("1d6+5")
    expected_dice = Dice(rolls=1, sides=6)
    expected_oper = "+"
    expected_int  = 5

    assert len(actual) == 3
    assert actual[0] == expected_dice
    assert actual[1] == expected_oper
    assert actual[2] == expected_int


def test_term_dice_with_flag_and_operator():
    token = term()
    actual = token.parseString("1d6!keep+5")
    expected_dice = Dice(rolls=1, sides=6)
    expected_flag = "!keep"
    expected_oper = "+"
    expected_int  = 5

    assert len(actual) == 4
    assert actual[0] == expected_dice
    assert actual[1] == expected_flag
    assert actual[2] == expected_oper
    assert actual[3] == expected_int


def test_term_dice_with_flag_and_operator_uppercase():
    token = term()
    actual = token.parseString("1D6!KEEP+5")
    expected_dice = Dice(rolls=1, sides=6)
    expected_flag = "!keep"
    expected_oper = "+"
    expected_int  = 5

    assert len(actual) == 4
    assert actual[0] == expected_dice
    assert actual[1] == expected_flag
    assert actual[2] == expected_oper
    assert actual[3] == expected_int


def test_term_dice_with_flag_and_operator_invalid():
    token = term()
    with pytest.raises(ParseException):
        token.parseString("1d6!keeper+5")
    with pytest.raises(ParseException):
        token.parseString("1d6a!keep+5")
    with pytest.raises(ParseException):
        token.parseString("1d6!advant+5")
