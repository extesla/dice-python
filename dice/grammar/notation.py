"""Roll20-compatible dice notation grammar using pyparsing.

Produces a typed AST of RollTerm objects.
"""

from __future__ import annotations

from pyparsing import (
    CaselessKeyword,
    CaselessLiteral,
    Combine,
    Forward,
    Group,
    Literal,
    Optional,
    Regex,
    Suppress,
    Word,
    alphanums,
    alphas,
    infixNotation,
    nums,
    opAssoc,
)

from dice.grammar.parse_actions import (
    make_add_sub,
    make_dice_term,
    make_float,
    make_function,
    make_integer,
    make_mul_div,
    make_parenthetical,
)

# ---------------------------------------------------------------------------
# Primitives
# ---------------------------------------------------------------------------

_integer = Word(nums).setParseAction(make_integer).setName("integer")

_float_num = Regex(r"\d+\.\d+").setParseAction(make_float).setName("float")

_number = (_float_num | _integer).setName("number")

# ---------------------------------------------------------------------------
# Compare points  (used inside modifiers, not standalone)
# ---------------------------------------------------------------------------

_compare_op = Regex(r">=|<=|>|<|=")
_compare_point = Combine(_compare_op + Word(nums)).setName("compare_point")

# ---------------------------------------------------------------------------
# Modifier suffixes — captured as raw strings, parsed by modifiers.parser
# ---------------------------------------------------------------------------

_keep_mod = Combine(
    (CaselessLiteral("kh") | CaselessLiteral("kl") | CaselessLiteral("k"))
    + Optional(Word(nums))
)

_drop_mod = Combine(
    (CaselessLiteral("dh") | CaselessLiteral("dl"))
    + Optional(Word(nums))
)

_explode_mod = Combine(
    (Literal("!!") | Literal("!p") | Literal("!"))
    + Optional(_compare_point)
)

_reroll_mod = Combine(
    (CaselessLiteral("ro") | CaselessLiteral("r"))
    + Optional(_compare_point)
)

_modifier = (_keep_mod | _drop_mod | _explode_mod | _reroll_mod).setName("modifier")

# ---------------------------------------------------------------------------
# Dice expression:  [count] 'd' sides [modifiers...]
# ---------------------------------------------------------------------------

_dice_count = Word(nums).setResultsName("count").setName("dice_count")
_dice_sides = (
    CaselessLiteral("F")
    | CaselessLiteral("fate")
    | Literal("%")
    | Word(nums)
).setResultsName("sides").setName("dice_sides")

_dice_expr = Group(
    Optional(_dice_count)
    + Suppress(CaselessLiteral("d"))
    + _dice_sides
    + Group(Optional(_modifier + Optional(_modifier + Optional(_modifier + Optional(_modifier)))))
    .setResultsName("modifiers")
).setParseAction(make_dice_term).setName("dice_expr")

# ---------------------------------------------------------------------------
# Forward-declare expression for recursive grammar
# ---------------------------------------------------------------------------

_expression = Forward().setName("expression")

# ---------------------------------------------------------------------------
# Parenthetical:  '(' expression ')'
# ---------------------------------------------------------------------------

_lparen = Suppress(Literal("("))
_rparen = Suppress(Literal(")"))
_parenthetical = Group(
    _lparen + _expression + _rparen
).setParseAction(make_parenthetical).setName("parenthetical")

# ---------------------------------------------------------------------------
# Function call:  floor(...) | ceil(...) | round(...) | abs(...)
# ---------------------------------------------------------------------------

_func_name = (
    CaselessKeyword("floor")
    | CaselessKeyword("ceil")
    | CaselessKeyword("round")
    | CaselessKeyword("abs")
)

_function_call = Group(
    _func_name + _lparen + _expression + _rparen
).setParseAction(make_function).setName("function_call")

# ---------------------------------------------------------------------------
# Factor (atom):  dice | function | parenthetical | number
# ---------------------------------------------------------------------------

_factor = (_dice_expr | _function_call | _parenthetical | _number).setName("factor")

# ---------------------------------------------------------------------------
# Flavor text:  [some text]
# ---------------------------------------------------------------------------

_flavor = (
    Suppress(Literal("["))
    + Regex(r"[^\]]*")
    + Suppress(Literal("]"))
).setResultsName("flavor").setName("flavor_text")

# ---------------------------------------------------------------------------
# Full expression with operator precedence via infixNotation
# ---------------------------------------------------------------------------

_mul_op = Literal("*") | Literal("/")
_add_op = Literal("+") | Literal("-")

_full_expression = infixNotation(
    _factor,
    [
        (_mul_op, 2, opAssoc.LEFT, make_mul_div),
        (_add_op, 2, opAssoc.LEFT, make_add_sub),
    ],
)

_expression <<= _full_expression  # type: ignore[operator]

# ---------------------------------------------------------------------------
# Top-level: expression with optional flavor text
# ---------------------------------------------------------------------------

_top_level = _full_expression + Optional(_flavor)


def parse_notation(text: str) -> tuple[list, str | None]:
    """Parse *text* and return ``(term_list, flavor_or_none)``.

    The term_list contains RollTerm objects ready to be wrapped in a
    RollExpression.  Flavor text (e.g. ``[attack]``) is returned
    separately.
    """
    result = _top_level.parseString(text, parseAll=True)

    flavor: str | None = None
    if "flavor" in result:
        raw = result["flavor"]
        # pyparsing may return a ParseResults list; take the first element
        if hasattr(raw, "__getitem__") and not isinstance(raw, str):
            raw = raw[0]
        flavor = str(raw).strip() or None

    # Collect all RollTerm objects from the parse result
    from dice.terms.base import RollTerm

    terms: list[RollTerm] = []
    for item in result:
        if isinstance(item, RollTerm):
            terms.append(item)
        elif isinstance(item, list):
            terms.extend(item)

    return terms, flavor
