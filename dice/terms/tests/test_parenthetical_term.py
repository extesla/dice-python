from dice.rng import SeededRNG
from dice.terms import (
    DiceTerm,
    NumericTerm,
    OperatorTerm,
    ParentheticalTerm,
)


def test_parenthetical_term_kind():
    pt = ParentheticalTerm(expression="(1+2)", children=[])
    assert pt.kind == "parenthetical_term"


def test_parenthetical_term_evaluate_numeric():
    rng = SeededRNG(0)
    children = [
        NumericTerm(value=3),
        OperatorTerm(operator="+"),
        NumericTerm(value=4),
    ]
    pt = ParentheticalTerm(expression="(3+4)", children=children)
    pt.evaluate(rng)
    assert pt.total == 7


def test_parenthetical_term_with_dice():
    rng = SeededRNG(42)
    dt = DiceTerm(count=1, faces=6)
    children = [
        dt,
        OperatorTerm(operator="+"),
        NumericTerm(value=5),
    ]
    pt = ParentheticalTerm(expression="(1d6+5)", children=children)
    pt.evaluate(rng)
    assert pt.total == dt.total + 5


def test_parenthetical_term_subtraction():
    rng = SeededRNG(0)
    children = [
        NumericTerm(value=10),
        OperatorTerm(operator="-"),
        NumericTerm(value=3),
    ]
    pt = ParentheticalTerm(expression="(10-3)", children=children)
    pt.evaluate(rng)
    assert pt.total == 7


def test_parenthetical_term_to_dict():
    rng = SeededRNG(0)
    children = [
        NumericTerm(value=2, id="n1"),
        OperatorTerm(operator="*", id="op1"),
        NumericTerm(value=3, id="n2"),
    ]
    pt = ParentheticalTerm(expression="(2*3)", children=children, id="pt1")
    pt.evaluate(rng)
    d = pt.to_dict()
    assert d["id"] == "pt1"
    assert d["kind"] == "parenthetical_term"
    assert d["expression"] == "(2*3)"
    assert d["total"] == 6
    assert len(d["children"]) == 3


def test_parenthetical_term_single_child():
    rng = SeededRNG(0)
    children = [NumericTerm(value=42)]
    pt = ParentheticalTerm(expression="(42)", children=children)
    pt.evaluate(rng)
    assert pt.total == 42
