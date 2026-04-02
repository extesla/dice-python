import pytest
from pyparsing import ParseException

from dice.grammar import integer


def test_integer():
    token = integer()
    actual = token.parseString("1")
    assert len(actual) == 1
    assert actual[0] == 1


def test_integer_against_alpha():
    token = integer()
    with pytest.raises(ParseException):
        token.parseString("a")
