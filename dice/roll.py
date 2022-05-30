from .grammar import expression, flags, operator
from .operators import (
    Add,
    Advantage,
    Disadvantage,
    Divide,
    Drop,
    Keep,
    Multiply,
    Subtract,
)
from .tokens import Dice, Integer
from pyparsing import infixNotation, opAssoc
import re


class Roll:
    """An object that represents the roll and its results."""

    @property
    def result(self):
        return self._result

    def __init__(self, expression: str):
        self.expression = expression

    def evaluate(self, tokens):
        """Evaluate the stack of tokens.

        This is a first pass at the evaluation function. We could improve it with
        generators and other techniques, but it is most important to have
        something that actually works as expected first.
        """
        # TODO: The result here should not be a scalar, but rather a result.
        result = None
        prev_token = None

        #: Iterate over the tokens passed for evaluation. This will continue until
        #: we have no more tokens to evaluate or we return out of the function.
        #:
        #: Our tokens can be grouped together, resulting in subexpressions that
        #: need to be evaluated. [SWQ]
        while tokens:

            #: Get the current token from the end of the list. We end up
            #: unraveling the tokens list right to left.
            cur_token = tokens.pop()
            cur_token_type = type(cur_token)

            #: If our current token is an array, we should recursively evaluate
            #: it. This means that we'll result inner arrays as we encounter them.
            if cur_token_type is type([]):
                return self.evaluate(cur_token)
            elif cur_token_type is Integer:
                result = int(cur_token.evaluate())
                print(f"> {result}")
            elif cur_token_type is Dice:
                result = cur_token.evaluate()
                print(f"> {result} ({result.total})")
                result = result.total
            elif cur_token in [
                "!advantage",
                "!adv",
                "!disadvantage",
                "!dis",
                "!keep",
                "!take",
                "!drop",
                "!shrink",
                "!grow",
            ]:
                next_token = tokens.pop()
                result = self.handle_flags(cur_token, next_token)
                print(f"> {result}")
            elif cur_token in ["+", "-", "*", "/"]:
                next_token = tokens.pop()
                result = self.handle_operator(cur_token, next_token, prev_token)
                print(f"> {result}")
            prev_token = cur_token
        return result

    def handle_flags(self, flag, expr):
        if flag in ("!advantage", "!adv"):
            t = Advantage(expr)
        elif flag in ("!disadvantage", "!dis"):
            t = Disadvantage(expr)
        elif flag in ("!drop"):
            t = Drop(expr)
        elif flag in ("!keep"):
            t = Keep(expr)
        return t.evaluate()

    def handle_operand(self, operand):
        """Evaluates an operand on either the left or right of an operator."""
        operand_type = type(operand)
        if operand_type == type([]):
            result = self.evaluate(operand)
        elif operand_type is Integer:
            result = int(operand.evaluate())
        elif operand_type is Dice:
            result = (operand.evaluate()).total
        return result

    def handle_operator(self, op, left, right):
        left = self.handle_operand(left)
        print(f"> .. {left}")

        print(f"> .. {str(op)}")

        right = self.handle_operand(right)
        print(f"> .. {right}")

        if str(op) == "+":
            t = Add(left, right)
        if str(op) == "-":
            t = Subtract(left, right)
        if str(op) == "*":
            t = Multiply(left, right)
        if str(op) == "/":
            t = Divide(left, right)
        return int(t.evaluate())

    def roll(self):
        parsed = parse_expression_using_infix_notation(self.expression)
        self._result = self.evaluate(parsed.asList())
        return self


def parse_expression_using_infix_notation(expr):
    infix_expression = infixNotation(expression(), [
        (flags(), 1, opAssoc.LEFT,),
        (operator(), 2, opAssoc.LEFT,),
    ])
    return infix_expression.parseString(expr)


def roll(text: str) -> list:
    """Roll dice represented by the text expression."""
    results = []
    expressions = re.split(r"[,;]", text)
    for expr in expressions:
        roll_obj = Roll(expr)
        result = (roll_obj.roll()).result
        results.append(result)
    return results
