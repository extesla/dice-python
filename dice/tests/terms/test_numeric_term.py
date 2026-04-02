from dice.rng import SeededRNG
from dice.terms import NumericTerm


def test_numeric_term_kind():
    nt = NumericTerm(value=5)
    assert nt.kind == "numeric_term"


def test_numeric_term_total():
    nt = NumericTerm(value=42)
    assert nt.total == 42


def test_numeric_term_float():
    nt = NumericTerm(value=3.5)
    assert nt.total == 3.5


def test_numeric_term_evaluate_is_noop():
    rng = SeededRNG(0)
    nt = NumericTerm(value=7)
    result = nt.evaluate(rng)
    assert result is nt
    assert nt.total == 7


def test_numeric_term_to_dict():
    nt = NumericTerm(value=10, id="num123")
    d = nt.to_dict()
    assert d == {
        "id": "num123",
        "kind": "numeric_term",
        "value": 10,
    }


def test_numeric_term_zero():
    nt = NumericTerm(value=0)
    assert nt.total == 0


def test_numeric_term_negative():
    nt = NumericTerm(value=-3)
    assert nt.total == -3
