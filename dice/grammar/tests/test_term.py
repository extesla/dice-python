import pytest
from pyparsing import ParseException

from dice.grammar import term
from dice.tokens import Dice


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
    # NOTE:  this is the same as in test_term_dice_only as CaselessLiteral will
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
