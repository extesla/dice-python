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
from dice.grammar import dice_sides
from pyparsing import ParseException
import pytest


def test_dice_sides_fate():
    token = dice_sides()
    actual = token.parseString("fate")
    assert len(actual) == 1
    assert actual[0] == "fate"


def test_dice_sides_fate_abbr():
    token = dice_sides()
    actual = token.parseString("F")
    assert len(actual) == 1
    assert actual[0] == "f"


def test_dice_sides_numeric():
    token = dice_sides()
    actual = token.parseString("20")
    assert len(actual) == 1
    assert actual[0] == 20


def test_dice_sides_against_alpha():
    token = dice_sides()
    with pytest.raises(ParseException):
        token.parseString("invalid")
