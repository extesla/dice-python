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
from pyparsing import (ParseException, StringStart, StringEnd)
import pytest


def flags_only():
    return StringStart() + flags() + StringEnd()


def test_flags_adv():
    token = flags()
    actual = token.parseString("!adv")
    assert len(actual) == 1
    assert actual[0] == "!adv"


def test_flags_adv_invalid():
    token = flags_only()
    with pytest.raises(ParseException):
        token.parseString("!advant")


def test_flags_adv_mixed_case():
    token = flags()
    actual = token.parseString("!aDv")
    assert len(actual) == 1
    assert actual[0] == "!adv"


def test_flags_adv_uppercase():
    token = flags()
    actual = token.parseString("!ADV")
    assert len(actual) == 1
    assert actual[0] == "!adv"


def test_flags_advantage():
    token = flags()
    actual = token.parseString("!advantage")
    assert len(actual) == 1
    assert actual[0] == "!advantage"


def test_flags_advantage_mixed_case():
    token = flags()
    actual = token.parseString("!aDvAnTaGe")
    assert len(actual) == 1
    assert actual[0] == "!advantage"


def test_flags_advantage_uppercase():
    token = flags()
    actual = token.parseString("!ADVANTAGE")
    assert len(actual) == 1
    assert actual[0] == "!advantage"


def test_flags_dis():
    token = flags()
    actual = token.parseString("!dis")
    assert len(actual) == 1
    assert actual[0] == "!dis"


def test_flags_dis_invalid():
    token = flags_only()
    with pytest.raises(ParseException):
        token.parseString("!disadv")


def test_flags_dis_mixed_case():
    token = flags()
    actual = token.parseString("!dIs")
    assert len(actual) == 1
    assert actual[0] == "!dis"


def test_flags_dis_uppercase():
    token = flags()
    actual = token.parseString("!DIS")
    assert len(actual) == 1
    assert actual[0] == "!dis"


def test_flags_disadvantage():
    token = flags()
    actual = token.parseString("!disadvantage")
    assert len(actual) == 1
    assert actual[0] == "!disadvantage"


def test_flags_disadvantage_mixed_case():
    token = flags()
    actual = token.parseString("!dIsAdVaNtAgE")
    assert len(actual) == 1
    assert actual[0] == "!disadvantage"


def test_flags_disadvantage_uppercase():
    token = flags()
    actual = token.parseString("!DISADVANTAGE")
    assert len(actual) == 1
    assert actual[0] == "!disadvantage"


def test_flags_drop():
    token = flags()
    actual = token.parseString("!drop")
    assert len(actual) == 1
    assert actual[0] == "!drop"


def test_flags_drop_invalid():
    token = flags_only()
    with pytest.raises(ParseException):
        token.parseString("!drops")


def test_flags_drop_mixed_case():
    token = flags()
    actual = token.parseString("!dRoP")
    assert len(actual) == 1
    assert actual[0] == "!drop"


def test_flags_drop_uppercase():
    token = flags()
    actual = token.parseString("!DROP")
    assert len(actual) == 1
    assert actual[0] == "!drop"


def test_flags_grow():
    token = flags()
    actual = token.parseString("!grow")
    assert len(actual) == 1
    assert actual[0] == "!grow"


def test_flags_grow_invalid():
    token = flags_only()
    with pytest.raises(ParseException):
        token.parseString("!grows")


def test_flags_grow_mixed_case():
    token = flags()
    actual = token.parseString("!gRoW")
    assert len(actual) == 1
    assert actual[0] == "!grow"


def test_flags_grow_uppercase():
    token = flags()
    actual = token.parseString("!GROW")
    assert len(actual) == 1
    assert actual[0] == "!grow"


def test_flags_keep():
    token = flags()
    actual = token.parseString("!keep")
    assert len(actual) == 1
    assert actual[0] == "!keep"


def test_flags_keep_invalid():
    token = flags_only()
    with pytest.raises(ParseException):
        token.parseString("!keeps")


def test_flags_keep_mixed_case():
    token = flags()
    actual = token.parseString("!kEeP")
    assert len(actual) == 1
    assert actual[0] == "!keep"


def test_flags_keep_uppercase():
    token = flags()
    actual = token.parseString("!KEEP")
    assert len(actual) == 1
    assert actual[0] == "!keep"


def test_flags_shrink():
    token = flags()
    actual = token.parseString("!shrink")
    assert len(actual) == 1
    assert actual[0] == "!shrink"


def test_flags_shrink_invalid():
    token = flags_only()
    with pytest.raises(ParseException):
        token.parseString("!shrinks")


def test_flags_shrink_mixed_case():
    token = flags()
    actual = token.parseString("!sHrInK")
    assert len(actual) == 1
    assert actual[0] == "!shrink"


def test_flags_shrink_uppercase():
    token = flags()
    actual = token.parseString("!SHRINK")
    assert len(actual) == 1
    assert actual[0] == "!shrink"


def test_flags_take():
    token = flags()
    actual = token.parseString("!take")
    assert len(actual) == 1
    assert actual[0] == "!take"


def test_flags_take_invalid():
    token = flags_only()
    with pytest.raises(ParseException):
        token.parseString("!takes")


def test_flags_take_mixed_case():
    token = flags()
    actual = token.parseString("!tAkE")
    assert len(actual) == 1
    assert actual[0] == "!take"


def test_flags_take_uppercase():
    token = flags()
    actual = token.parseString("!TAKE")
    assert len(actual) == 1
    assert actual[0] == "!take"


def test_flags_unknown_token():
    token = flags()
    with pytest.raises(ParseException):
        token.parseString("!shoop")
