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
from dice.grammar import dice
from pyparsing import ParseException
import unittest


class DiceGrammarTest(unittest.TestCase):
    """
    """

    def test_dice(self):
        token = dice()
        actual = token.parseString("1d6")
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual[0], 1)
        self.assertEqual(actual[1], "d")
        self.assertEqual(actual[2], 6)

    def test_dice_uppercase(self):
        token = dice()
        actual = token.parseString("1D6")
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual[0], 1)
        self.assertEqual(actual[1], "d")
        self.assertEqual(actual[2], 6)

    def test_dice_implicit_rolls(self):
        token = dice()
        actual = token.parseString("d20")
        self.assertEqual(len(actual), 2)
        self.assertEqual(actual[0], "d")
        self.assertEqual(actual[1], 20)

    def test_dice_fate(self):
        token = dice()
        actual = token.parseString("3dfate")
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual[0], 3)
        self.assertEqual(actual[1], "d")
        self.assertEqual(actual[2], "fate")

    def test_dice_fate_abbr(self):
        token = dice()
        actual = token.parseString("3dF")
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual[0], 3)
        self.assertEqual(actual[1], "d")
        self.assertEqual(actual[2], "f") #ZR: Expected to be lowercase as defined in grammar.py


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(DiceGrammarTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
