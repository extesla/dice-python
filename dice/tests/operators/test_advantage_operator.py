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
from dice.operators import Advantage
from dice.tokens import Dice
import pytest


def test_instantiate_advantage_operator():
    operator = Advantage([5, 17])
    assert operator.original_operands == ([5, 17],)
    assert operator.operands == ([5, 17],)


def test_repr():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Advantage operator on operands
    When the method __repr__ is called
    Then the result should be "Advantage"
    """
    operator = Advantage([5, 17])
    assert repr(operator) == "Advantage([5, 17])"


def test_advantage_function_when_choosing_from_empty_array():
    operator = Advantage()
    with pytest.raises(IndexError):
        operator.function([])


def test_advantage_function_with_invalid_iterable():
    operator = Advantage()
    with pytest.raises(TypeError):
        operator.function(1)


def test_advantage_function_with_no_iterable():
    operator = Advantage()
    with pytest.raises(TypeError):
        operator.function(None)


def test_evaluate_advantage_with_single_value_in_scalar_array():
    operator = Advantage([5, 17])
    actual = operator.evaluate()

    assert actual == 17
    assert operator.result == 17
    assert actual == operator.result


def test_evaluate_advantage_with_multiple_values_in_scalar_array():
    operator = Advantage([13, 5, 17])
    actual = operator.evaluate()

    assert actual == 17
    assert operator.result == 17
    assert actual == operator.result


def test_evaluate_advantage_with_dice_token_value(mocker):
    mock_random = mocker.patch("dice.tokens.mt_rand")
    mock_random.side_effect = [5, 17]

    dice_token = Dice(sides=20, rolls=2)
    operator = Advantage(dice_token)
    actual = operator.evaluate()

    assert actual == 17
    assert operator.result == 17
    assert actual == operator.result
