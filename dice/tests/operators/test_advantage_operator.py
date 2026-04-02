import pytest

from dice.operators import Advantage
from dice.tokens import Dice


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
