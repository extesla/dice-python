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
from dice.grammar import flags
from pprint import pprint
from pyparsing import (ParseException, StringStart, StringEnd)
import unittest


def flags_only():
    return StringStart() + flags() + StringEnd()


class FlagsGrammarTest(unittest.TestCase):
    """
    """
    def test_flags_adv(self):
        token = flags()
        actual = token.parseString("!adv")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!adv")

    def test_flags_adv_invalid(self):
        token = flags_only()
        with self.assertRaises(ParseException):
            token.parseString("!advant")

    def test_flags_adv_mixed_case(self):
        token = flags()
        actual = token.parseString("!aDv")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!adv")

    def test_flags_adv_uppercase(self):
        token = flags()
        actual = token.parseString("!ADV")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!adv")

    def test_flags_advantage(self):
        token = flags()
        actual = token.parseString("!advantage")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!advantage")

    def test_flags_advantage_mixed_case(self):
        token = flags()
        actual = token.parseString("!aDvAnTaGe")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!advantage")

    def test_flags_advantage_uppercase(self):
        token = flags()
        actual = token.parseString("!ADVANTAGE")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!advantage")

    def test_flags_dis(self):
        token = flags()
        actual = token.parseString("!dis")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!dis")

    def test_flags_dis_invalid(self):
        token = flags_only()
        with self.assertRaises(ParseException):
            actual = token.parseString("!disadv")

    def test_flags_dis_mixed_case(self):
        token = flags()
        actual = token.parseString("!dIs")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!dis")

    def test_flags_dis_uppercase(self):
        token = flags()
        actual = token.parseString("!DIS")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!dis")

    def test_flags_disadvantage(self):
        token = flags()
        actual = token.parseString("!disadvantage")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!disadvantage")

    def test_flags_disadvantage_mixed_case(self):
        token = flags()
        actual = token.parseString("!dIsAdVaNtAgE")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!disadvantage")

    def test_flags_disadvantage_uppercase(self):
        token = flags()
        actual = token.parseString("!DISADVANTAGE")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!disadvantage")

    def test_flags_drop(self):
        token = flags()
        actual = token.parseString("!drop")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!drop")

    def test_flags_drop_invalid(self):
        token = flags_only()
        with self.assertRaises(ParseException):
            actual = token.parseString("!drops")

    def test_flags_drop_mixed_case(self):
        token = flags()
        actual = token.parseString("!dRoP")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!drop")

    def test_flags_drop_uppercase(self):
        token = flags()
        actual = token.parseString("!DROP")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!drop")

    def test_flags_grow(self):
        token = flags()
        actual = token.parseString("!grow")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!grow")

    def test_flags_grow_invalid(self):
        token = flags_only()
        with self.assertRaises(ParseException):
            actual = token.parseString("!grows")

    def test_flags_grow_mixed_case(self):
        token = flags()
        actual = token.parseString("!gRoW")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!grow")

    def test_flags_grow_uppercase(self):
        token = flags()
        actual = token.parseString("!GROW")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!grow")

    def test_flags_keep(self):
        token = flags()
        actual = token.parseString("!keep")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!keep")

    def test_flags_keep_invalid(self):
        token = flags_only()
        with self.assertRaises(ParseException):
            actual = token.parseString("!keeps")

    def test_flags_keep_mixed_case(self):
        token = flags()
        actual = token.parseString("!kEeP")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!keep")

    def test_flags_keep_uppercase(self):
        token = flags()
        actual = token.parseString("!KEEP")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!keep")

    def test_flags_shrink(self):
        token = flags()
        actual = token.parseString("!shrink")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!shrink")

    def test_flags_shrink_invalid(self):
        token = flags_only()
        with self.assertRaises(ParseException):
            actual = token.parseString("!shrinks")

    def test_flags_shrink_mixed_case(self):
        token = flags()
        actual = token.parseString("!sHrInK")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!shrink")

    def test_flags_shrink_uppercase(self):
        token = flags()
        actual = token.parseString("!SHRINK")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!shrink")

    def test_flags_take(self):
        token = flags()
        actual = token.parseString("!take")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!take")

    def test_flags_take_invalid(self):
        token = flags_only()
        with self.assertRaises(ParseException):
            actual = token.parseString("!takes")

    def test_flags_take_mixed_case(self):
        token = flags()
        actual = token.parseString("!tAkE")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!take")

    def test_flags_take_uppercase(self):
        token = flags()
        actual = token.parseString("!TAKE")
        self.assertEqual(len(actual), 1)
        self.assertEqual(actual[0], "!take")

    def test_flags_unknown_token(self):
        token = flags()
        with self.assertRaises(ParseException):
            actual = token.parseString("!shoop")


if __name__ == '__main__':
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(FlagsGrammarTest)
    suite = unittest.TestSuite(tests)

    unittest.TextTestRunner(descriptions=True, verbosity=5).run(suite)
