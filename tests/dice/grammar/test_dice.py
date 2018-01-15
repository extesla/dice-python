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
from pyparsing import ParseException
import pytest


def test_dice():
    token = dice()
    actual = token.parseString("1d6")
    assert len(actual) == 3
    assert actual[0] == 1
    assert actual[1] == "d"
    assert actual[2] == 6


def test_dice_uppercase():
    token = dice()
    actual = token.parseString("1D6")
    assert len(actual) == 3
    assert actual[0] == 1
    assert actual[1] == "d"
    assert actual[2] == 6


def test_dice_implicit_rolls():
    token = dice()
    actual = token.parseString("d20")
    assert len(actual) == 2
    assert actual[0] == "d"
    assert actual[1] == 20


def test_dice_fate():
    token = dice()
    actual = token.parseString("3dfate")
    assert len(actual) == 3
    assert actual[0] == 3
    assert actual[1] == "d"
    assert actual[2] == "fate"


def test_dice_fate_abbr():
    token = dice()
    actual = token.parseString("3dF")
    assert len(actual) == 3
    assert actual[0] == 3
    assert actual[1] == "d"
    assert actual[2] == "f" #ZR: Expected to be lowercase as defined in grammar.py
