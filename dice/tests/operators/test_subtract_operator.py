import pytest

from dice.operators import Subtract


def test_init():
    operator = Subtract(5, 1)
    assert operator.original_operands == (5, 1)
    assert operator.operands == (5, 1)


def test_repr():
    #: Test that the string representation of the operator is what is
    #: expected.
    #:
    #: Given an instance of the Subtract operator on operands 5 and 1
    #: When the method __repr__ is called
    #: Then the result should be "Add(5, 1)"
    operator = Subtract(5, 1)
    assert repr(operator) == "Subtract(5, 1)"


def test_str():
    #: Test that the string representation of the operator is what is
    #: expected.
    #:
    #: Given an instance of the Subtract operator on operands 5 and 1
    #: When the method __repr__ is called
    #: Then the result should be "Add(5, 1)"
    operator = Subtract(5, 1)
    assert str(operator) == "5-1"


def test_evaluate():
    #: Test that the evaluation of the operator is correct.
    #:
    #: Given an instance of the Subtract operator on operands 5 and 1
    #: When the operator is evaluated
    #: Then the result should be 4
    operator = Subtract(5, 1)
    actual = operator.evaluate()
    assert actual == 4


def test_evaluate_invalid():
    #: Test that the evaluation of the operator raises a ValueError
    #: when an invalid term is supplied.
    #:
    #: Given an instance of the Subtract operator on operands 5 and
    #:     "invalid"
    #: When the operator is evaluated
    #: Then a ValueError should be raised.
    operator = Subtract(5, "invalid")
    with pytest.raises(ValueError):
        operator.evaluate()


def test_evaluate_operand_as_integral_string():
    #: Test that the evaluation of the operator is correct on all
    #: numeric operands, even if one of those operands is represtend
    #: as a string.
    #:
    #: Given an instance of the Subtract operator on operands 5 and "2"
    #: When the operator is evaluated
    #: Then the result should be 7.
    operator = Subtract(5, "2")
    actual = operator.evaluate()
    assert actual == 3


def test_evaluate_object():
    pass


def test_function():
    # operator = Subtract()
    # operator.function()
    pass
