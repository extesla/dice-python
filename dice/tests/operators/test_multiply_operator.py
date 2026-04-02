import pytest

from dice.operators import Multiply


def test_init():
    operator = Multiply(5, 1)
    assert operator.original_operands == (5, 1)
    assert operator.operands == (5, 1)


def test_repr():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Multiply operator on operands 4 and 2
    When the method __repr__ is called
    Then the result should be "Add(4, 2)"
    """
    operator = Multiply(4, 2)
    assert repr(operator) == "Multiply(4, 2)"


def test_str():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Multiply operator on operands 4 and 2
    When the method __str__ is called
    Then the result should be "4*2"
    """
    operator = Multiply(4, 2)
    assert str(operator) == "4*2"


def test_evaluate():
    """
    Test that the evaluation of the operator is correct.

    Given an instance of the Multiply operator on operands 4 and 2
    When the operator is evaluated
    Then the result should be 4
    """
    operator = Multiply(4, 2)
    actual = operator.evaluate()
    assert actual == 8


def test_evaluate_invalid():
    """
    Test that the evaluation of the operator raises a ValueError
    when an invalid term is supplied.

    Given an instance of the Divide operator on operands 4 and
        "invalid"
    When the operator is evaluated
    Then a ValueError should be raised.
    """
    operator = Multiply(4, "invalid")
    with pytest.raises(ValueError):
        operator.evaluate()


def test_evaluate_operand_as_integral_string():
    """
    Test that the evaluation of the operator is correct on all
    numeric operands, even if one of those operands is represtend
    as a string.

    Given an instance of the Subtract operator on operands 4 and "3"
    When the operator is evaluated
    Then the result should be 7.
    """
    operator = Multiply(4, "3")
    actual = operator.evaluate()
    assert actual == 12


def test_evaluate_object():
    pass


def test_function():
    # operator = Multiply()
    # operator.function()
    pass
