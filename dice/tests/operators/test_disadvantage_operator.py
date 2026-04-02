import pytest

from dice.operators import Disadvantage
from dice.tokens import Dice


def test_instantiate_disadvantage_operator():
    operator = Disadvantage([17, 3])
    assert operator.original_operands == ([17, 3],)
    assert operator.operands == ([17, 3],)


def test_repr():
    """
    Test that the string representation of the operator is what is
    expected.

    Given an instance of the Disdvantage operator on operands
    When the method __repr__ is called
    Then the result should be "Disdvantage"
    """
    operator = Disadvantage([17, 3])
    assert repr(operator) == "Disadvantage([17, 3])"


def test_disadvantage_function_when_choosing_from_empty_array():
    operator = Disadvantage()
    with pytest.raises(IndexError):
        operator.function([])


def test_disadvantage_function_with_invalid_iterable():
    operator = Disadvantage()
    with pytest.raises(TypeError):
        operator.function(1)


def test_disadvantage_function_with_no_iterable():
    operator = Disadvantage()
    with pytest.raises(TypeError):
        operator.function(None)


def test_evaluate_disadvantage_with_single_value_in_scalar_array():
    operator = Disadvantage([5, 17])
    actual = operator.evaluate()

    assert actual == 5
    assert operator.result == 5
    assert actual == operator.result


def test_evaluate_disadvantage_with_multiple_values_in_scalar_array():
    operator = Disadvantage([13, 5, 17])
    actual = operator.evaluate()

    assert actual == 5
    assert operator.result == 5
    assert actual == operator.result


def test_evaluate_disadvantage_with_dice_token_value(mocker):
    mock_random = mocker.patch("dice.tokens.mt_rand")
    mock_random.side_effect = [5, 17]

    dice_token = Dice(sides=20, rolls=2)
    operator = Disadvantage(dice_token)
    actual = operator.evaluate()

    assert actual == 5
    assert operator.result == 5
    assert actual == operator.result
