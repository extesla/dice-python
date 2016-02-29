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
from dice.grammar import operator
from pyparsing import ParseException
import unittest


class OperatorGrammarTest(unittest.TestCase):
    """
    """

    def test_operator_addition(self):
        token = operator()
        actual = token.parseString("+")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "+")

    def test_operator_division(self):
        token = operator()
        actual = token.parseString("/")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "/")

    def test_operator_multiplication(self):
        token = operator()
        actual = token.parseString("*")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "*")

    def test_operator_subtraction(self):
        token = operator()
        actual = token.parseString("-")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "-")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(OperatorGrammarTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
