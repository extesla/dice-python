import pytest

from dice.operators import Grow


def test_init():
    operator = Grow(5, 1)
    assert operator.original_operands == (5, 1)
    assert operator.operands == (5, 1)


def test_repr():
    operator = Grow(5, 1)
    assert repr(operator) == "Grow(5, 1)"


def test_evaluate():
    pass


def test_evaluate_object():
    pass


def test_function():
    # operator = Grow()
    # operator.function()
    pass
