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
import logging
import random

#: Module logger
logger = logging.getLogger(__name__)

def classname(obj):
    """Returns the name of an objects class"""
    return obj.__class__.__name__


def mt_rand(min, max):
    """
    Mersenne Twist pseudo random number generator (PRNG) that has value-safe
    operations for the minimum value.

    :param min: the lower boundary of the random number range.
    :type min: int
    :param max: the upper boundary of the random number range.
    :type max: int
    """
    if min is None:
        warn("Minimum value not specified, assuming minimum value of 1")
        min = 1
    if max is None:
        raise TypeError("Random requires a maximum boundary. Given: None")
    return random.randint(min, max)


def to_int(obj, default=0):
    """
    Value-safe conversion of an object to an ``int``. If the ``obj`` being
    converted is either ``None`` or an empty string, the object will be
    assigned the value of ``default``.

    :param obj: the object being cast as an integer.
    :param default: the default value to
    """
    try:
        return int(obj)
    except (TypeError, ValueError):
        return int(default)
