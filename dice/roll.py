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


def handle_flags(flag, expr):
    if flag in ("!advantage", "!adv"):
        t = Advantage(expr)
    elif flag in ("!disadvantage", "!dis"):
        t = Disadvantage(expr)
    elif flag in ("!drop"):
        t = Drop(expr)
    elif flag in ("!keep"):
        t = Keep(expr)
    return t.evaluate()


def handle_operator(op, left, right):
    left_type = type(left)
    if left_type == type([]):
        left = evaluate(left)
    elif left_type is Integer:
        left = int(left.evaluate())
    elif left_type is Dice:
        left = (left.evaluate()).total

    right_type = type(left)
    if right_type == type([]):
        right = evaluate(right)
    elif right_type is Integer:
        right = int(left.evaluate())
    elif right_type is Dice:
        right = (left.evaluate()).total

    if str(op) == "+":
        t = Add(left, right)
    if str(op) == "-":
        t = Subtract(left, right)
    if str(op) == "*":
        t = Multiply(left, right)
    if str(op) == "/":
        t = Divide(left, right)
    return int(t.evaluate())


def evaluate(tokens):
    """
    Evaluate the stack of tokens.

    This is a first pass at the evaluation function. We could improve it with
    generators and other techniques, but it is most important to have
    something that actually works as expected first.
    """
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
            return evaluate(cur_token)
        elif cur_token_type is Integer:
            result = int(cur_token.evaluate())
        elif cur_token_type is Dice:
            result = (cur_token.evaluate()).total
        elif cur_token in ["!advantage", "!adv", "!disadvantage", "!dis", "!keep", "!take", "!drop", "!shrink", "!grow"]:
            next_token = tokens.pop()
            result = handle_flags(cur_token, next_token)
        elif cur_token in ["+", "-", "*", "/"]:
            next_token = tokens.pop()
            result = handle_operator(cur_token, next_token, prev_token)
        prev_token = cur_token
    return result


def roll(text):
    """
    """
    infix_expression = infixNotation(expression(), [
        (flags(), 1, opAssoc.LEFT,),
        (operator(), 2, opAssoc.LEFT,),
    ])

    results = []
    parts = re.split(r'[,;]', text)
    for part in parts:
        parsed = infix_expression.parseString(part)
        results.append(evaluate(parsed.asList()))
    return results
