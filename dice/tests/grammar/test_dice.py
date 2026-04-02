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
from dice.grammar import dice
from dice.tokens import Dice
from pyparsing import ParseException
import pytest


def test_dice_grammar():
    token = dice()
    actual = token.parseString("1d6")
    expected = Dice(rolls=1, sides=6)

    assert len(actual) == 1
    assert actual[0] == expected
    assert actual[0].rolls == expected.rolls
    assert actual[0].sides == expected.sides


def test_dice_grammar_with_uppercase():
    token = dice()
    actual = token.parseString("1D6")
    expected = Dice(rolls=1, sides=6)

    assert len(actual) == 1
    assert actual[0] == expected
    assert actual[0].rolls == expected.rolls
    assert actual[0].sides == expected.sides


def test_dice_grammaer_with_implicit_rolls():
    token = dice()
    actual = token.parseString("d20")
    expected = Dice(rolls=1, sides=20)

    assert len(actual) == 1
    assert actual[0] == expected
    assert actual[0].rolls == expected.rolls
    assert actual[0].sides == expected.sides


def test_dice_grammar_with_fate_dice():
    token = dice()
    actual = token.parseString("3dfate")
    expected = Dice(rolls=3, sides="fate")

    assert len(actual) == 1
    assert actual[0] == expected
    assert actual[0].rolls == expected.rolls
    assert actual[0].sides == expected.sides


def test_dice_grammar_with_fate_dice_abbr():
    token = dice()
    actual = token.parseString("3dF")
    # ZR: Expected to be lowercase as defined in grammar.py
    expected = Dice(rolls=3, sides="f")

    assert len(actual) == 1
    assert actual[0] == expected
    assert actual[0].rolls == expected.rolls
    assert actual[0].sides == expected.sides


def test_dice_grammar_with_invalid_format():
    token = dice()
    with pytest.raises(ParseException):
        token.parseString("1dZ")
