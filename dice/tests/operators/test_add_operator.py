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
from dice.operators import Add
import pytest


def test_instantiate_add_operator():
    operator = Add(5, 1)
    assert operator.original_operands == (5, 1)
    assert operator.operands == (5, 1)


def test_add_operator_repr():
    """
    Test that the add operator's ``__repr__`` returns the expected string.

    Given an instance of the Add operator on operands 5 and 1
    When the method __repr__ is called
    Then the result should be "Add(5, 1)"
    """
    operator = Add(5, 1)
    assert repr(operator) == "Add(5, 1)"


def test_add_operator_repr():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Add operator on operands 5 and 1
    When the method __repr__ is called
    Then the result should be "5+1"
    """
    operator = Add(5, 1)
    assert str(operator) == "5+1"


def test_evaluate():
    """
    Test that the evaluation of the operator is correct.

    Given an instance of the Add operator on operands 5 and 1
    When the operator is evaluated
    Then the result should be 6.
    """
    operator = Add(5, 1)
    actual = operator.evaluate()
    assert actual == 6


def test_evaluate_invalid():
    """
    Test that the evaluation of the operator raises a ValueError
    when an invalid term is supplied.

    Given an instance of the Add operator on operands 5 and "invalid"
    When the operator is evaluated
    Then a ValueError should be raised.
    """
    operator = Add(5, "invalid")
    with pytest.raises(ValueError):
        operator.evaluate()


def test_evaluate_operand_as_integral_string():
    """
    Test that the evaluation of the operator is correct on all
    numeric operands, even if one of those operands is represtend
    as a string.

    Given an instance of the Add operator on operands 5 and "2"
    When the operator is evaluated
    Then the result should be 7.
    """
    operator = Add(5, "2")
    actual = operator.evaluate()
    assert actual == 7


def test_evaluate_object():
    pass


def test_function():
    # operator = Add()
    # operator.function()
    pass
