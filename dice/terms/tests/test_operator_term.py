import pytest

from dice.rng import SeededRNG
from dice.terms import OperatorTerm


def test_operator_term_kind():
    ot = OperatorTerm(operator="+")
    assert ot.kind == "operator_term"


def test_operator_term_valid_operators():
    for op in ["+", "-", "*", "/"]:
        ot = OperatorTerm(operator=op)
        assert ot.operator == op


def test_operator_term_invalid_operator():
    with pytest.raises(ValueError, match="Invalid operator"):
        OperatorTerm(operator="%")


def test_operator_term_total_raises():
    ot = OperatorTerm(operator="+")
    with pytest.raises(TypeError):
        _ = ot.total


def test_operator_term_evaluate_is_noop():
    rng = SeededRNG(0)
    ot = OperatorTerm(operator="-")
    result = ot.evaluate(rng)
    assert result is ot


def test_operator_term_to_dict():
    ot = OperatorTerm(operator="*", id="op123")
    d = ot.to_dict()
    assert d == {
        "id": "op123",
        "kind": "operator_term",
        "operator": "*",
    }
