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
        """
        Evaluates an operator against operands.

        The operands are each evaluated through the :class:`Token`'s
        ``evaluate_object`` function. Once the operands have been resolved
        they are fed into the operator's function.

        :return: The result of the operator.
        :rtype int:
        """
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
    def function(self, minuend, subtrahend):
        """
        Subtracts the subtrahend from the minuend.

        :param minuend: Left hand value of the operation.
        :type minuend: int
        :param minuend: Right hand value of the operation.
        :return: The result of the difference from the given values.
        """
        result = operator.sub(minuend, subtrahend)
        if result < 1:
            return 1
        return result

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
    Operator to keep the ``n`` number of highest scores.

    The keep operator will retain the highest ``n`` values in an iterable
    dropping the rest. The expression ``3d6!keep(2)`` reads as: "roll 3d6 and
    keep the two highest dice rolls".

    The operator literal, ``!keep`` takes a single argument indicating the
    number of values to keep.

    >>> operator = Keep([5, 2, 8], 2)
    >>> operator.evaluate()
    [8, 5]
    """
    def function(self, iterable, n):
        #: If we're indicating that we don't want to keep anything (!keep(0))
        #: or we want to keep fewer than nothing (!keep(-2)) then we should
        #: just short circuit out of this and return an empty array.
        if n <= 0:
            return []

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
    def function(self, iterable):
        result = sorted(iterable, reverse=True)[:1]
        if result:
            return result[0]
        raise IndexError("Unable to select advantaged result from: {}".format(result))

    def __repr__(self):
        """
        The ``Advantage`` operator has a custom __repr__.
        """
        return "Advantage({0})".format(*self.original_operands)


# @operator(literal="!dis")
# @operator(literal="!disadvantage")
class Disadvantage(Operator):
    """

    E.g.::

    2d20!dis
    2d20+5!disadvantage
    """
    def function(self, iterable):
        result = sorted(iterable)[:1]
        if result:
            return result[0]
        raise IndexError("Unable to select disadvantaged result from: {}".format(result))

    def __repr__(self):
        """
        The ``Disadvantage`` operator has a custom __repr__.
        """
        return "Disadvantage({0})".format(*self.original_operands)


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
