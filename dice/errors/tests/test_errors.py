import pytest

from dice.errors import (
    DiceError,
    DiceExecutionError,
    DiceParseError,
    DiceValidationError,
)


def test_dice_error_str():
    err = DiceError(code="E001", message="something went wrong")
    assert str(err) == "[E001] something went wrong"


def test_dice_error_is_exception():
    err = DiceError(code="E001", message="bad")
    assert isinstance(err, Exception)


def test_dice_error_optional_fields():
    err = DiceError(code="E001", message="bad", position=5, expression="2d6+1")
    assert err.position == 5
    assert err.expression == "2d6+1"


def test_dice_error_defaults():
    err = DiceError(code="E001", message="bad")
    assert err.position is None
    assert err.expression is None


def test_dice_parse_error_is_dice_error():
    err = DiceParseError(code="P001", message="parse failed")
    assert isinstance(err, DiceError)


def test_dice_execution_error_is_dice_error():
    err = DiceExecutionError(code="X001", message="exec failed")
    assert isinstance(err, DiceError)


def test_dice_validation_error_is_dice_error():
    err = DiceValidationError(code="V001", message="invalid")
    assert isinstance(err, DiceError)


def test_dice_error_can_be_raised_and_caught():
    with pytest.raises(DiceError):
        raise DiceParseError(code="P001", message="bad input")


def test_subclass_can_be_caught_by_parent():
    with pytest.raises(DiceError):
        raise DiceExecutionError(code="X001", message="limit exceeded")
