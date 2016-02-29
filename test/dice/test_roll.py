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
from dice import roll
from mock import patch
import unittest


class RollFunctionTest(unittest.TestCase):
    """
    """

    def test_roll_1d6(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        with patch("random.randint") as mock_randint:
            mock_randint.return_value = 3
            actual = roll("1d6")
            self.assertEqual(actual, 3)
            mock_randint.assert_called_once_with(6)

    def test_roll_3d6(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        with patch("random.randint") as mock_randint:
            mock_randint.return_value = 3
            actual = roll("3d6")
            self.assertEqual(actual, 3)
            mock_randint.assert_called_once_with(6)

    def test_roll_1d20_addition(self):
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

    def test_roll_1d20_addition_with_spaces(self):
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

    def test_roll_2d20_advantage(self):
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

    def test_roll_2d20_advantage_with_modifiers(self):
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

    def test_roll_2d20_disadvantage(self):
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

    def test_roll_2d20_disadvantage_with_modifiers(self):
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

    def test_roll_1d20_divide(self):
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

    def test_roll_1d20_divide_to_integer(self):
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

    def test_roll_1d20_divide_with_spaces(self):
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

    def test_roll_1d20_multiply(self):
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

    def test_roll_1d20_multiply_with_spaces(self):
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

    def test_roll_1d20_subtraction(self):
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

    def test_roll_1d20_subtraction_floor(self):
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

    def test_roll_1d20_subtraction_with_spaces(self):
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

    def test_roll_1dF(self):
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

    def test_roll_d20(self):
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

if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(RollFunctionTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
