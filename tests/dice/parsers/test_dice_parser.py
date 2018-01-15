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
from dice.parsers import DiceParser
import pytest


def test_match():
    """
    Test that the Dice method "match" returns the expected
    dice term value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "1d6" is passed into the
        "match" method of the Dice class
    Then the returned string should be "1d6"
    """
    parser = DiceParser()
    actual = parser.match("1d6")
    assert actual == "1d6"

def test_match_complex_noparens():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the DiceParser class
    When the dice roll expression "1d20+5+2d6+2" is passed into the
        "match" method of the Dice class
    Then the returned string should be "1d20"
    """
    parser = DiceParser()
    actual = parser.match("1d20+5+2d6+2")
    assert actual == "1d20"

def test_match_complex_parens():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the DiceParser class
    When the complex dice roll expression "(1d20+5)+2d6+2" is passed
        into the "match" method of the Dice class
    Then the returned string should be "1d6"
    """
    parser = DiceParser()
    actual = parser.match("(1d20+5)+2d6+2")
    assert actual == "1d20"

def test_match_raises_value_error_on_invalid_expression():
    """
    Test that the :class:`DiceParser` method "match" raises a
    :class:`ValueError` if the expression it is attempting to parse is not
    a valid dice roll expression.

    Given the DiceParser class
    When the dice roll expression "1+2" is passed into the "match"
        method of the Dice class
    Then a ValueError should be raised
    """
    parser = DiceParser()

    with pytest.raises(ValueError):
        parser.match("1+2")

def test_match_with_flag():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "2d20!advantage" is passed into the
        "match" method of the Dice class
    Then the returned string should be "2d20"
    """
    parser = DiceParser()
    actual = parser.match("2d20!advantage")
    assert actual == "2d20"

def test_match_with_modifier():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "1d6+2" is passed into the "match"
        method of the Dice class
    Then the returned string should be "1d6"
    """
    parser = DiceParser()
    actual = parser.match("1d6+2")
    assert actual == "1d6"

def test_parse():
    parser = DiceParser()
    actual, rolls, sides = parser.parse("1d6")
    assert actual == "1d6"
    assert rolls == 1
    assert sides == 6

def test_parse_no_rolls():
    parser = DiceParser()
    actual, rolls, sides = parser.parse("d6")
    assert actual == "d6"
    assert rolls == 1
    assert sides == 6

def test_parse_with_flag():
    parser = DiceParser()
    actual, rolls, sides = parser.parse("1d6!advantage")
    assert actual == "1d6"
    assert rolls == 1
    assert sides == 6

def test_parse_with_modifier():
    parser = DiceParser()
    actual, rolls, sides = parser.parse("1d6+2")
    assert actual == "1d6"
    assert rolls == 1
    assert sides == 6

def test_pattern():
    parser = DiceParser()
    actual = parser.pattern
    assert actual == r"^.*?(?P<term>\d*[dD][\dF]+){1}.*?$"

def test_trim():
    """
    Test that the Dice method "match" returns the expected
    dice term value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "1d6" is passed into the
        "match" method of the Dice class
    Then the returned string should be "1d6"
    """
    parser = DiceParser()
    actual = parser.trim("1d6")
    assert actual == "1d6"

def test_trim_complex_noparens():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "1d20+5+2d6+2" is passed into the
        "match" method of the Dice class
    Then the returned string should be "1d20"
    """
    parser = DiceParser()
    actual = parser.trim("1d20+5+2d6+2")
    assert actual == "1d20"

def test_trim_complex_parens():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the Dice class
    When the complex dice roll expression "(1d20+5)+2d6+2" is passed
        into the "match" method of the Dice class
    Then the returned string should be "1d6"
    """
    parser = DiceParser()
    actual = parser.trim("(1d20+5)+2d6+2")
    assert actual == "1d20"

def test_trim_no_match():
    """
    Test that the Dice method "match" returns the expected
    dice term value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "1d6+2" is passed into the "match"
        method of the Dice class
    Then the returned string should be "1d6"
    """
    with pytest.raises(ValueError):
        parser = DiceParser()
        actual = parser.trim("1+2")

def test_trim_with_flag():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "2d20!advantage" is passed into the
        "match" method of the Dice class
    Then the returned string should be "2d20"
    """
    parser = DiceParser()
    actual = parser.trim("2d20!advantage")
    assert actual == "2d20"

def test_trim_with_modifier():
    """
    Test that the Dice method "match" returns the expected dice term
    value when fed a dice roll expression.

    Given the Dice class
    When the dice roll expression "1d6+2" is passed into the "match"
        method of the Dice class
    Then the returned string should be "1d6"
    """
    parser = DiceParser()
    actual = parser.trim("1d6+2")
    assert actual == "1d6"
