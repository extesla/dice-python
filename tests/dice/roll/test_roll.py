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
from mock import patch
import pytest


def test_roll_1d6(mocker):
    """
    Assert that when 1d6 is rolled, that the expected value is returned.
    """
    mock_randint = mocker.patch("random.randint")
    mock_randint.return_value = 3

    actual = roll("1d6")
    assert actual == 3
    mock_randint.assert_called_once_with(6)


def test_roll_3d6(mocker):
    """
    Assert that when 3d6 is rolled, that the expected value is returned.
    """
    mock_randint = mocker.patch("random.randint")
    mock_randint.return_value = 3

    actual = roll("3d6")
    assert actual == 3
    mock_randint.assert_called_once_with(6)


def test_roll_1d20_addition(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 17
        actual = roll("1d20+5")
        self.assertEqual(actual, 22)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_addition_with_spaces(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 18
        actual = roll("1d20  + 5")
        self.assertEqual(actual, 23)
        mock_randint.assert_called_once_with(20)


def test_roll_2d20_advantage(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 17
        actual = roll("2d20!advantage")
        self.assertEqual(actual, 22)
        mock_randint.assert_called_once_with(20)


def test_roll_2d20_advantage_with_modifiers(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 17
        actual = roll("(2d20+5)!advantage")
        self.assertEqual(actual, 22)
        mock_randint.assert_called_once_with(20)


def test_roll_2d20_disadvantage(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 17
        actual = roll("2d20!disadvantage")
        self.assertEqual(actual, 22)
        mock_randint.assert_called_once_with(20)


def test_roll_2d20_disadvantage_with_modifiers(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 17
        actual = roll("(2d20+5)!disadvantage")
        self.assertEqual(actual, 22)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_divide(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("1d20/5")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_divide_to_integer(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("1d20/5")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_divide_with_spaces(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("1d20 / 5")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_multiply(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("1d20*5")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_multiply_with_spaces(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("1d20  * 5")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_subtraction(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 12
        actual = roll("1d20-5")
        self.assertEqual(actual, 7)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_subtraction_floor(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 2
        actual = roll("1d20-5")
        self.assertEqual(actual, 1)
        mock_randint.assert_called_once_with(20)


def test_roll_1d20_subtraction_with_spaces(mocker):
    #: TBW
    #:
    #: Given
    #: When
    #: Then
    with patch("random.randint") as mock_randint:
        mock_randint.return_value = 3
        actual = roll("1d20  - 5")
        self.assertEqual(actual, 3)
        mock_randint.assert_called_once_with(20)


def test_roll_1dF(mocker):
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


def test_roll_d20(mocker):
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
