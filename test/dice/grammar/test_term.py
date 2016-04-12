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
from dice.grammar import term
from pprint import pprint
from pyparsing import ParseException
import unittest


class TermGrammarTest(unittest.TestCase):
    """
    """

    def test_term_dice_only(self):
        token = term()
        actual = token.parseString("1d6")
        pprint(actual.asList())
        self.assertEqual(len(actual), 3)
        self.assertEqual(actual.asList(), [1, 'd', 6])

    def test_term_dice_only_invalid(self):
        token = term()
        with self.assertRaises(ParseException):
            actual = token.parseString("1d1.2")
        with self.assertRaises(ParseException):
            actual = token.parseString("1d-6")
        with self.assertRaises(ParseException):
            actual = token.parseString("1t6")

    def test_term_dice_only_uppercase(self):
        token = term()
        actual = token.parseString("1D6")
        pprint(actual.asList())
        self.assertEqual(len(actual), 3)
        #NOTE:  this is the same as in test_term_dice_only as CaselessLiteral will
        # return the case of the defined matchString, not the search string passed
        # into parse.   -ZR
        self.assertEqual(actual.asList(), [1, 'd', 6])

    def test_term_dice_with_flag(self):
        token = term()
        actual = token.parseString("1d6!keep")
        pprint(actual.asList())
        self.assertEqual(len(actual), 4)
        self.assertEqual(actual.asList(), [1, 'd', 6, '!keep'])

    def test_term_dice_with_operator(self):
        token = term()
        actual = token.parseString("1d6+5")
        pprint(actual.asList())
        self.assertEqual(len(actual), 5)
        self.assertEqual(actual.asList(), [1, 'd', 6, '+', 5])

    def test_term_dice_with_flag_and_operator(self):
        token = term()
        actual = token.parseString("1d6!keep+5")
        pprint(actual.asList())
        self.assertEqual(len(actual), 6)
        self.assertEqual(actual.asList(), [1, 'd', 6, '!keep', '+', 5])

    def test_term_dice_with_flag_and_operator_uppercase(self):
        token = term()
        actual = token.parseString("1D6!KEEP+5")
        pprint(actual.asList())
        self.assertEqual(len(actual), 6)
        self.assertEqual(actual.asList(), [1, 'd', 6, '!keep', '+', 5])

    def test_term_dice_with_flag_and_operator_invalid(self):
        token = term()
        with self.assertRaises(ParseException):
            actual = token.parseString("1d6!keeper+5")
        with self.assertRaises(ParseException):
            actual = token.parseString("1d6a!keep+5")
        with self.assertRaises(ParseException):
            actual = token.parseString("1d6!advant+5")



if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TermGrammarTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
