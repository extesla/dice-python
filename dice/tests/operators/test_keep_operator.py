import pytest

from dice.operators import Keep
from dice.tokens import Dice


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
    assert actual == [4, 5]
    assert operator.result == [4, 5]
    assert actual == operator.result


def test_evaluate_keep_with_dice_token_values(mocker):
    mock_random = mocker.patch("dice.tokens.mt_rand")
    mock_random.side_effect = [2, 5, 1, 4, 3]

    dice_token = Dice(sides=6, rolls=5)
    operator = Keep(dice_token, 2)

    actual = operator.evaluate()
    assert actual == [4, 5]
    assert operator.result == [4, 5]
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
