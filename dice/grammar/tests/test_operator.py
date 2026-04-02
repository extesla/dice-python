import pytest
from pyparsing import ParseException

from dice.grammar import operator


def test_operator_addition():
    token = operator()
    actual = token.parseString("+")
    assert len(actual) == 1
    assert actual[0] == "+"


def test_operator_division():
    token = operator()
    actual = token.parseString("/")
    assert len(actual) == 1
    assert actual[0] == "/"


def test_operator_multiplication():
    token = operator()
    actual = token.parseString("*")
    assert len(actual) == 1
    assert actual[0] == "*"


def test_operator_subtraction():
    token = operator()
    actual = token.parseString("-")
    assert len(actual) == 1
    assert actual[0] == "-"
