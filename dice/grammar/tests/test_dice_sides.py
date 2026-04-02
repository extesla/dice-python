import pytest
from pyparsing import ParseException

from dice.grammar import dice_sides


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
