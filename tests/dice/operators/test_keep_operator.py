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
from dice.operators import Keep
from dice.tokens import Dice
import pytest


def test_instantiate_Keep_operator():
    operator = Keep([5, 2, 1, 4], 2)
    assert operator.original_operands == ([5, 2, 1, 4], 2)
    assert operator.operands == ([5, 2, 1, 4], 2)


def test_repr():
    operator = Keep([5, 2, 1, 4], 2)
    assert repr(operator) == "Keep([5, 2, 1, 4], 2)"


def test_evaluate_keep_with_scalar_values():
    operator = Keep([5, 2, 1, 4], 2)
    actual = operator.evaluate()
    assert actual == [5, 4]
    assert operator.result == [5, 4]
    assert actual == operator.result


def test_evaluate_keep_with_dice_token_values(mocker):
    mock_random = mocker.patch("dice.tokens.mt_rand")
    mock_random.side_effect = [2, 5, 1, 4, 3]

    dice_token = Dice(sides=6, rolls=5)
    operator = Keep(dice_token, 2)

    actual = operator.evaluate()
    assert actual == [5, 4]
    assert operator.result == [5, 4]
    assert actual == operator.result


def test_keep_function_when_keeping_more_values_than_exist():
    operator = Keep()
    actual = operator.function([1, 2, 3], 5)
    assert actual == [1, 2, 3]


def test_keep_function_when_keeping_zero_values():
    operator = Keep()
    actual = operator.function([1, 2, 3], 0)
    assert actual == []


def test_keep_function_with_invalid_iterable():
    operator = Keep()
    with pytest.raises(TypeError):
        operator.function(1, 1)


def test_keep_function_with_no_iterable():
    operator = Keep()
    with pytest.raises(TypeError):
        operator.function(None, 1)
