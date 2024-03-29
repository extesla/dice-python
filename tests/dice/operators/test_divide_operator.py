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
from dice.operators import Divide
import pytest


def test_instantiate_divide_operator():
    operator = Divide(5, 1)
    assert operator.original_operands == (5, 1)
    assert operator.operands == (5, 1)


def test_divide_operator_repr():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Divide operator on operands 6 and 2
    When the method __repr__ is called
    Then the result should be "Divide(6, 2)"
    """
    operator = Divide(6, 2)
    assert repr(operator) == "Divide(6, 2)"


def test_divide_operator_str():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Divide operator on operands 6 and 2
    When the method __repr__ is called
    Then the result should be "Divide(6, 2)"
    """
    operator = Divide(6, 2)
    assert str(operator) == "6/2"


def test_evaluate():
    """
    Test that the evaluation of the operator is correct.

    Given an instance of the Divide operator on operands 6 and 2
    When the operator is evaluated
    Then the result should be 3.
    """
    operator = Divide(6, 2)
    actual = operator.evaluate()
    assert actual == 3


def test_evaluate_divide_by_zero():
    """
    Test that the evaluation of the operator results in a
    divide-by-zero error being raised.

    Given an instance of the Subtract operator on operands 6 and 0
    When the operator is evaluated
    Then a ZeroDivisionError is raised
    """
    operator = Divide(6, 0)
    with pytest.raises(ZeroDivisionError):
        operator.evaluate()


def test_evaluate_invalid():
    """
    Test that the evaluation of the operator raises a ValueError
    when an invalid term is supplied.

    Given an instance of the Divide operator on operands 6 and
        "invalid"
    When the operator is evaluated
    Then a ValueError should be raised.
    """
    operator = Divide(6, "invalid")
    with pytest.raises(ValueError):
        operator.evaluate()


def test_evaluate_operand_as_integral_string():
    """
    Test that the evaluation of the operator is correct on all
    numeric operands, even if one of those operands is represtend
    as a string.

    Given an instance of the Subtract operator on operands 6 and "3"
    When the operator is evaluated
    Then the result should be 7.
    """
    operator = Divide(6, "3")
    actual = operator.evaluate()
    assert actual == 2


def test_evaluate_object():
    pass


def test_function():
    # operator = Divide()
    # operator.function()
    pass
