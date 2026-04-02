import pytest
from pyparsing import ParseException

from dice.grammar import dice
from dice.tokens import Dice


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
