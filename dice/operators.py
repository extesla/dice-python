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
from dice.tokens import Token, Integer
from dice.utils import classname
import random
import operator


class Operator(Token):
    """
    An ``Operator`` is a token that represents all operations that can be
    performed on ``Terms`` within an expression.

    Operators represent both unary mathematical operations (e.g. addition,
    subtraction, division, multiplication, etc.) as well as flag operations
    (e.g. advantage, disadvantage, drop, keep, etc.).

    Operators always come after the dice roll expression (e.g. ``1d6``) and
    may be prefixed by any number of spaces. Action operations are

    Unary operators (e.g. ``+``, ``-``, ``*``, and ``/``) and term operators
    (e.g. ``drop``, ``keep``, ``advantage``, etc.) are both supported.

    :param original_operands: the original, immutable, operands passed to
        the operator when it was initialized.
    :type original_operands: tuple
    :param operands: the operands that will be operated on.
    :type operands: tuple
    """

    @classmethod
    def parse(cls, string, location, tokens):
        return cls(*tokens)

    def __init__(self, *operands):
        self.operands = self.original_operands = operands

    def __repr__(self):
        return "{0}({1})".format(
            classname(self), ', '.join(map(str, self.original_operands)))

    def evaluate(self):
        self.operands = map(self.evaluate_object, self.operands)
        self.result = self.function(*self.operands)
        return self.result

    @property
    def function(self):
        raise NotImplementedError("Operator subclass has no function")


class IntegerOperator(Operator):
    def evaluate_object(self, obj):
        return super(IntegerOperator, self).evaluate_object(obj, Integer)


# @operator(literal="/")
class Divide(IntegerOperator):
    function = operator.floordiv

    def __str__(self):
        return "{}".format("/".join(map(str, self.original_operands)))


# @operator(literal="*")
class Multiply(IntegerOperator):
    function = operator.mul

    def __str__(self):
        return "{}".format("*".join(map(str, self.original_operands)))

# @operator(literal="-")
class Subtract(IntegerOperator):
    function = operator.sub

    def __str__(self):
        return "{}".format("-".join(map(str, self.original_operands)))

# @operator(literal="+")
class Add(IntegerOperator):
    function = operator.add

    def __str__(self):
        return "{}".format("+".join(map(str, self.original_operands)))

# @operator(literal="!total")
class Total(Operator):
    function = sum


# @operator(literal="!drop")
class Drop(Operator):
    """
    Operator to drop the ``n`` number of lowest scores.

    The drop operator will drop the lowest ``n`` values in an iterable keeping
    the rest. The expression ``3d6!drop(2)`` reads as: "roll 3d6 and drop the
    two lowest dice rolls".

    The operator literal, ``!drop`` takes a single argument indicating the
    number of values to drop.

    >>> operator = Drop([5, 2, 8], 2)
    >>> operator.evaluate()
    [8]
    """
    def function(self, iterable, n):
        for die in sorted(iterable)[:n]:
            iterable.remove(die)
        return iterable

    def literal(self):
        return "drop"


# @operator(literal="!keep")
# @operator(literal="!take")
class Keep(Operator):
    """
    Operator to keep the ``n`` highest dice rolls. E.g. ``3d6 keep 1``
    """
    def function(self, iterable, n):
        for die in sorted(iterable)[:-n]:
            iterable.remove(die)
        return iterable


# @operator(literal="!adv")
# @operator(literal="!advantage")
class Advantage(Operator):
    """

    E.g.::

    2d20!adv
    2d20+5!advantage
    """
    pass


# @operator(literal="!dis")
# @operator(literal="!disadvantage")
class Disadvantage(Operator):
    """

    E.g.::

    2d20!dis
    2d20+5!disadvantage
    """
    pass


# @operator(literal="!reroll")
class Reroll(Operator):
    """

    E.g.::

    1d20!reroll 1
    1d20+5!reroll 1,2
    1d20+5!reroll 1-5
    1d20+5!reroll 1,2,18-20
    """
    pass


# @operator(literal="!grow")
class Grow(Operator):
    """

    E.g.::

    1d20!grow 1
    """
    pass


# @operator(literal="!shrink")
class Shrink(Operator):
    """

    E.g.::

    1d20!shrink 1
    """
    pass
