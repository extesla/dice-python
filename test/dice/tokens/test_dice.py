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
from dice.tokens import Dice
from mock import patch
import unittest


class DiceTest(unittest.TestCase):
    """
    """

    def test_init(self):
        #: TBW
        #:
        #: Given
        #: When
        #: Then
        token = Dice(value="1d6", rolls=1, sides=6)
        self.assertEqual(token.value, "1d6")
        self.assertEqual(token.rolls, 1)
        self.assertEqual(token.sides, 6)
        self.assertEqual(token.result, None)

    def test_repr(self):
        #: Test that the string representation of the operator is what is
        #: expected.
        #:
        #: Given an instance of the Add operator on operands 5 and 1
        #: When the method __repr__ is called
        #: Then the result should be "Add(5, 1)"
        token = Dice(value="1d6", rolls=1, sides=6)
        self.assertEqual(repr(token), "Dice(1d6)")

    def test_repr(self):
        #: Test that the string representation of the operator is what is
        #: expected.
        #:
        #: Given an instance of the Add operator on operands 5 and 1
        #: When the method __repr__ is called
        #: Then the result should be "Add(5, 1)"
        token = Dice(value="1d6", rolls=1, sides=6)
        self.assertEqual(str(token), "1d6")

    def test_evaluate(self):
        #: Test that the string representation of the operator is what is
        #: expected.
        #:
        #: Given an instance of the Add operator on operands 5 and 1
        #: When the method __repr__ is called
        #: Then the result should be "Add(5, 1)"
        token = Dice(value="1d6", rolls=1, sides=6)
        with patch("dice.tokens.mt_rand") as mock_random:
            mock_random.return_value = 4
            token.evaluate()
            self.assertEqual(token.result, [4])
            mock_random.assert_called_once_with(min=1, max=6)

    def test_roll(self):
        #: Test
        #:
        #: Given
        #: When
        #: Then
        with patch("dice.tokens.mt_rand") as mock_random:
            mock_random.return_value = 4
            actual = Dice.roll(1, 6)
            self.assertEqual(len(actual), 1)
            self.assertEqual(actual, [4])
            mock_random.assert_called_once_with(min=1, max=6)



if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(DiceTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
