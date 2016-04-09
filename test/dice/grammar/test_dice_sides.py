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
from dice.grammar import dice_sides
from pyparsing import ParseException
import unittest


class DiceSidesGrammarTest(unittest.TestCase):
    """
    """
    def test_dice_sides_fate(self):
        token = dice_sides()
        actual = token.parseString("fate")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "fate")

    def test_dice_sides_fate_abbr(self):
        token = dice_sides()
        actual = token.parseString("F")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "f")

    def test_dice_sides_numeric(self):
        token = dice_sides()
        actual = token.parseString("20")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], 20)

    def test_dice_sides_against_alphaZ(self):
        token = dice_sides()
        self.assertRaises(ParseException, token.parseString, "invalid")


    def test_dice_sides_against_alpha(self):
        token = dice_sides()
        with self.assertRaises(ParseException) as context:
            token.parseString("invalid")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(DiceSidesGrammarTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
