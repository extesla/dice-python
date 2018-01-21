# The MIT License (MIT)
#
# Copyright (c) 2016 Sean Quinn
#
# Permision is hereby granted, free of charge, to any person obtaining a
# copy of this software and asociated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permision notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPREs OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNEs FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
from dice.tokens import Dice
import pytest

def test_initialize_dice():
    token = Dice(rolls=1, sides=6)
    assert token.rolls == 1
    assert token.sides == 6
    assert token.results is None
    assert token.total == 0

def test_dice_repr():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Dice token with the value "1d6"
    When the method __repr__ is called
    Then the results should be "Dice(rolls=1, sides=6)"
    """
    token = Dice(rolls=1, sides=6)
    assert repr(token) == "Dice(rolls=1, sides=6)"

def test_dice_str():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Dice token with the value "1d6"
    When the method __str__ is called
    Then the results should be "1d6"
    """
    token = Dice(rolls=1, sides=6)
    assert str(token) == "1d6"

def test_dice_evaluate(mocker):
    mock_mt_rand = mocker.patch("dice.tokens.mt_rand")
    mock_mt_rand.return_value = 4

    token = Dice(rolls=1, sides=6)
    token.evaluate()

    assert len(token.results) == 1
    assert token.results == [4]
    assert token.total == 4
    mock_mt_rand.assert_called_once_with(min=1, max=6)

def test_dice_roll(mocker):
    mock_mt_rand = mocker.patch("dice.tokens.mt_rand")
    mock_mt_rand.return_value = 4

    token = Dice(rolls=1, sides=6)
    actual = token.roll()

    assert len(actual) == 1
    assert actual == [4]
    mock_mt_rand.assert_called_once_with(min=1, max=6)
