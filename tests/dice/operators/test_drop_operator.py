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
from dice.operators import Drop
from dice.tokens import Dice
import pytest


def test_instantiate_drop_operator():
    operator = Drop([5, 2, 1, 4], 2)
    assert operator.original_operands == ([5, 2, 1, 4], 2)
    assert operator.operands == ([5, 2, 1, 4], 2)


def test_repr():
    operator = Drop([5, 2, 1, 4], 2)
    assert repr(operator) == "Drop([5, 2, 1, 4], 2)"


def test_evaluate_drop_with_scalar_values():
    operator = Drop([5, 2, 1, 4], 2)
    actual = operator.evaluate()
    assert actual == [4, 5]
    assert operator.result == [4, 5]
    assert actual == operator.result


def test_evaluate_drop_with_dice_token_values(mocker):
    mock_random = mocker.patch("dice.tokens.mt_rand")
    mock_random.side_effect = [2, 5, 1, 4, 3]

    dice_token = Dice(sides=6, rolls=5)
    operator = Drop(dice_token, 2)

    actual = operator.evaluate()
    assert actual == [3, 4, 5]
    assert operator.result == [3, 4, 5]
    assert actual == operator.result
    mock_random.assert_has_calls([
        mocker.call(min=1, max=6),
        mocker.call(min=1, max=6),
        mocker.call(min=1, max=6),
        mocker.call(min=1, max=6),
        mocker.call(min=1, max=6),
    ])


def test_drop_function_when_droping_more_values_than_exist():
    operator = Drop()
    actual = operator.function([1, 2, 3], 5)
    assert actual == []


def test_drop_function_when_droping_zero_values():
    operator = Drop()
    actual = operator.function([1, 2, 3], 0)
    assert actual == [1, 2, 3]


def test_drop_function_with_invalid_iterable():
    operator = Drop()
    with pytest.raises(TypeError):
        operator.function(1, 1)


def test_drop_function_with_no_iterable():
    operator = Drop()
    with pytest.raises(TypeError):
        operator.function(None, 1)
