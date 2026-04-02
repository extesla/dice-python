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
from dice.roll import roll
from pyparsing import ParseException
import pytest


@pytest.fixture
def mock_randint(mocker):
    _mock = mocker.patch("random.randint")
    return _mock


def test_roll_1d6(mock_randint):
    """
    Assert that when 1d6 is rolled, that the expected value is returned.
    """
    mock_randint.return_value = 3

    actual = roll("1d6")
    assert actual == [3]
    mock_randint.assert_called_once_with(1, 6)


def test_roll_3d6(mocker, mock_randint):
    """
    Assert that when 3d6 is rolled, that the expected value is returned.
    """
    mock_randint.side_effect = [3, 1, 4]

    actual = roll("3d6")
    assert actual == [8]
    mock_randint.assert_has_calls(
        [mocker.call(1, 6), mocker.call(1, 6), mocker.call(1, 6)]
    )


def test_roll_1d20_addition(mock_randint):
    mock_randint.return_value = 17

    actual = roll("1d20+5")
    assert actual == [22]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_addition_with_spaces(mock_randint):
    mock_randint.return_value = 17

    actual = roll("1d20  + 5")
    assert actual == [22]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_2d20_advantage(mocker, mock_randint):
    mock_randint.side_effect = [8, 15]

    actual = roll("2d20!advantage")
    assert actual == [15]
    mock_randint.assert_has_calls(
        [
            mocker.call(1, 20),
            mocker.call(1, 20),
        ]
    )


def test_roll_2d20_advantage_with_modifiers_after_flag(mocker, mock_randint):
    mock_randint.side_effect = [8, 15]

    actual = roll("2d20!advantage+5")
    assert actual == [20]
    mock_randint.assert_has_calls(
        [
            mocker.call(1, 20),
            mocker.call(1, 20),
        ]
    )


def test_roll_2d20_advantage_with_modifiers_before_flag(mock_randint):
    #: We currently don't support applying flags to an expression, only to
    #: the actual dice roll.
    with pytest.raises(ParseException):
        roll("2d20+5!advantage")


def test_roll_2d20_disadvantage(mocker, mock_randint):
    mock_randint.side_effect = [8, 15]

    actual = roll("2d20!disadvantage")
    assert actual == [8]
    mock_randint.assert_has_calls(
        [
            mocker.call(1, 20),
            mocker.call(1, 20),
        ]
    )


def test_roll_2d20_disadvantage_with_modifiers_after_flag(mocker, mock_randint):
    mock_randint.side_effect = [8, 15]

    actual = roll("2d20!disadvantage+5")
    assert actual == [13]
    mock_randint.assert_has_calls(
        [
            mocker.call(1, 20),
            mocker.call(1, 20),
        ]
    )


def test_roll_2d20_disadvantage_with_modifiers_before_flag(mock_randint):
    #: We currently don't support applying flags to an expression, only to
    #: the actual dice roll.
    with pytest.raises(ParseException):
        roll("2d20+5!disadvantage")


def test_roll_1d20_divide(mock_randint):
    mock_randint.return_value = 12

    actual = roll("1d20/3")
    assert actual == [4]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_divide_to_integer(mock_randint):
    mock_randint.return_value = 17

    actual = roll("1d20/3")
    assert actual == [5]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_divide_with_spaces(mock_randint):
    mock_randint.return_value = 12

    actual = roll("1d20 /  3")
    assert actual == [4]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_multiply(mock_randint):
    mock_randint.return_value = 6

    actual = roll("1d20*3")
    assert actual == [18]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_multiply_with_spaces(mock_randint):
    mock_randint.return_value = 6

    actual = roll("1d20  * 3")
    assert actual == [18]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_subtraction(mock_randint):
    mock_randint.return_value = 12

    actual = roll("1d20-5")
    assert actual == [7]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_subtraction_floor(mock_randint):
    mock_randint.return_value = 2

    actual = roll("1d20-5")
    assert actual == [1]
    mock_randint.assert_called_once_with(1, 20)


def test_roll_1d20_subtraction_with_spaces(mock_randint):
    mock_randint.return_value = 12

    actual = roll("1d20 -   5")
    assert actual == [7]
    mock_randint.assert_called_once_with(1, 20)


@pytest.mark.skip(reason="Not yet ready")
def test_roll_1dF(mock_randint):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("1dF")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(6)


@pytest.mark.skip(reason="Not yet ready")
def test_roll_d20(mock_randint):
    #: TBW
    #:
    #: Given the roll function
    #: When the roll function is called with the expression "d20"
    #: Then the expression should evaluate as if it were given the
    #:     expression: "1d20"
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("d20")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(20)
