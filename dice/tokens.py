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
from dice.utils import classname, mt_rand
import logging
import re
import six

#: The module logger.
logger = logging.getLogger(__name__)


class Token(object):
    """
    A ``Token`` is any discrete element of an expression. Tokens can be a
    ``Term`` or an ``Operator``.

    :param value: the term's value.
    :type value: str
    :param result: the result of the term's evaluation.
    :type result: mixed
    """

    #: The result of a token's evaluation.
    results = None

    def __init__(self, *args, **kwargs):
        #: This is a convenient way that we can make all of our tokens
        #: effectively factories for themselves. This will iterate over all
        #: of the keyword arguments passed into the token's constructor and
        #: assign them, assuming that a property exists for that property
        #: name. [SWQ]
        for prop, value in six.iteritems(kwargs):
            if hasattr(self, prop):
                setattr(self, prop, value)

    def evaluate(self):
        """
        Evaluate the current token, by default this is a no-op and classes
        that implement ``Token`` are expected to override this function.

        :return: self
        """
        return self

    def evaluate_cached(self, verbose=None):
        """
        Wraps evaluate(), caching results
        """
        if not hasattr(self, "results") or self.results is None:
            self.evaluate()
        logger.debug(str.format("Evaluating: {0} -> {1}", str(self), str(self.results)))
        return self

    def evaluate_object(self, obj, cls=None):
        """
        Evaluate an object, coercing them to a particular type if necessary.

        :param obj: the object to be evaluated, or coerced.
        :param cls: the type that the object should be cast to.
        """
        if isinstance(obj, Token):
            obj = obj.evaluate_cached()
        if cls is not None:
            obj = cls(obj)
        return obj


class Expression(Token):
    """
    An ``Expression`` is the model of an entire dice roll, including terms,
    operators, and interior expressions.

    An expression can be a simple command such as roll a six-sided die once,
    e.g.::

      1d6

    Represented as an actual ``Expression`` object, this might look like::

      Expression(tokens=[
          Dice(sides=6, rolls=1)
      ])

    It can be a compound command modifying a dice roll such as roll a
    twenty-sided die once and add five to result, e.g.::

      1d20+5

    Represented as an actual ``Expression`` object, this might look like::

      Expression(tokens=[
          Add(
            Dice(sides=20, rolls=1),
            Integer(5)
          )
      ])

    Or it can be an arbitrarily more complex command: roll two twenty-sided
    dice and add five to the result, take the higher of the two and add the
    result of the roll of two six-sided dice rerolling 1's and 2's, e.g.::

      (2d20+5)!advantage + 1d4;2d6!reroll(1,2)

    Represented as an actual ``Expression`` object, this might look like::

      Expression(tokens=[
          Expression(tokens=[
              Add(
                  Advantage(
                      Add(
                          Dice(sides=20, rolls=1),
                          Integer(5)
                      )
                  ),
                  Dice(sides=4, rolls=1)
              )
          ]),
          Expression(tokens=[
              Reroll(
                  Dice(sides=6, rolls=2),
                  [1, 2]
              )
          ])
      ])

    An expression is typically built by using an :class:`ExpressionParser` to
    convert a string into the arbitrarily complex representation of a dice
    expression.

    :param raw_text: The text of the expression, this is the exact string that
        was parsed to create the expression.
    :type text: str
    :param tokens:
    :type tokens: list
    """

    #: The raw text representing this expression. This is the original, and
    #: effectively immutable value that was parsed to result in the expression
    #: to be evaluated.
    _raw_text = None

    results = []

    #: The tokens, including subexpressions, that compose this expression.
    tokens = []

    @property
    def raw_text(self):
        return self._raw_text

    @raw_text.setter
    def raw_text(self, value):
        raise RuntimeError("Expression's raw text is immutable.")


class Term(Token):
    """
    ``Terms`` are the operands of an expression.

    Terms can be constant values, e.g. ``1``, ``2``, ``3``, or they can be a
    representation of a dice roll, e.g. ``1d6``, ``2d6``, ``1d20``, etc.

    :param value: the term's value.
    :type value: str
    """

    pass


class Dice(Term):
    """
    The ``Dice`` term is a representation of a group of dice to be rolled,
    all with the same number of sides, e.g. 1d6, 3d6, 2d20, etc.

    :param rolls: the lefthand side of the dice term, indicating the number
        of times that the die will be rolled.
    :type rolls: int
    :param sides: the righthand side of the dice term, indicating the number
        of sides that the dice has.
    :type sides: int
    """

    #: The number of times that a dice will be rolled. This is the
    #: lefthand side of the dice term, i.e. the number that precedes the
    #: side identifier (e.g. "d6").
    #:
    #: (Default: 1)
    rolls = None

    #: The number of sides for a dice. This is the righthand side of the
    #: dice term, e.g. "d6".
    sides = None

    #: The total, summed, value of the evaluation results.
    total = 0

    def __eq__(self, other):
        return self.sides == other.sides and self.rolls == other.rolls

    def __iter__(self):
        for x in self.results:
            yield x

    def __repr__(self):
        return "Dice(rolls={0!r}, sides={1!r})".format(self.rolls, self.sides)

    def __str__(self):
        return "{0!s}d{1!s}".format(self.rolls, self.sides)

    def evaluate(self):
        """
        Alias for ``roll``.
        """
        self.results = self.roll()
        self.total = sum(self.results)
        return self

    def roll(self):
        return [mt_rand(min=1, max=self.sides) for i in range(self.rolls)]


class Integer(int, Term):
    """A wrapper around the int class"""

    @classmethod
    def parse(cls, string, location, tokens):
        return cls(tokens[0])
