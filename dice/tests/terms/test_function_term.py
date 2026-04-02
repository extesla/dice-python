import pytest
from dice.rng import SeededRNG
from dice.terms import FunctionTerm, NumericTerm, OperatorTerm


def test_function_term_kind():
    ft = FunctionTerm(function="floor", children=[NumericTerm(value=3)])
    assert ft.kind == "function_term"


def test_function_term_floor():
    rng = SeededRNG(0)
    children = [
        NumericTerm(value=7),
        OperatorTerm(operator="/"),
        NumericTerm(value=2),
    ]
    ft = FunctionTerm(function="floor", children=children)
    ft.evaluate(rng)
    assert ft.total == 3  # floor(7 // 2) = 3


def test_function_term_abs():
    rng = SeededRNG(0)
    children = [NumericTerm(value=-5)]
    ft = FunctionTerm(function="abs", children=children)
    ft.evaluate(rng)
    assert ft.total == 5


def test_function_term_ceil():
    rng = SeededRNG(0)
    # With integer division, 7//2 = 3, ceil(3) = 3
    # Use a float to test ceil more meaningfully
    children = [NumericTerm(value=3)]
    ft = FunctionTerm(function="ceil", children=children)
    ft.evaluate(rng)
    assert ft.total == 3


def test_function_term_round():
    rng = SeededRNG(0)
    children = [NumericTerm(value=4)]
    ft = FunctionTerm(function="round", children=children)
    ft.evaluate(rng)
    assert ft.total == 4


def test_function_term_invalid():
    with pytest.raises(ValueError, match="Unsupported function"):
        FunctionTerm(function="sin", children=[])


def test_function_term_to_dict():
    rng = SeededRNG(0)
    children = [NumericTerm(value=-3, id="n1")]
    ft = FunctionTerm(function="abs", children=children, id="fn1")
    ft.evaluate(rng)
    d = ft.to_dict()
    assert d == {
        "id": "fn1",
        "kind": "function_term",
        "function": "abs",
        "children": [{"id": "n1", "kind": "numeric_term", "value": -3}],
        "total": 3,
    }
