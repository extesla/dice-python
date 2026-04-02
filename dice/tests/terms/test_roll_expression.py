from dice.rng import SeededRNG
from dice.terms import (
    DiceTerm,
    NumericTerm,
    OperatorTerm,
    RollExpression,
)


def test_roll_expression_kind():
    re = RollExpression(expression="1d6", children=[])
    assert re.kind == "roll_expression"


def test_roll_expression_simple_dice():
    rng = SeededRNG(42)
    dt = DiceTerm(count=2, faces=6)
    re = RollExpression(expression="2d6", children=[dt])
    re.evaluate(rng)
    assert re.total == dt.total


def test_roll_expression_dice_plus_modifier():
    rng = SeededRNG(42)
    dt = DiceTerm(count=1, faces=20)
    children = [
        dt,
        OperatorTerm(operator="+"),
        NumericTerm(value=5),
    ]
    re = RollExpression(expression="1d20+5", children=children)
    re.evaluate(rng)
    assert re.total == dt.total + 5


def test_roll_expression_with_label():
    rng = SeededRNG(42)
    dt = DiceTerm(count=1, faces=20)
    re = RollExpression(
        expression="1d20",
        children=[dt],
        label="attack roll",
    )
    re.evaluate(rng)
    d = re.to_dict()
    assert d["label"] == "attack roll"


def test_roll_expression_no_label_omitted():
    rng = SeededRNG(42)
    re = RollExpression(
        expression="5",
        children=[NumericTerm(value=5)],
    )
    re.evaluate(rng)
    d = re.to_dict()
    assert "label" not in d


def test_roll_expression_to_dict():
    rng = SeededRNG(42)
    dt = DiceTerm(count=1, faces=6, id="d1")
    re = RollExpression(expression="1d6", children=[dt], id="root")
    re.evaluate(rng)
    d = re.to_dict()
    assert d["id"] == "root"
    assert d["kind"] == "roll_expression"
    assert d["expression"] == "1d6"
    assert len(d["children"]) == 1
    assert d["children"][0]["kind"] == "dice_term"
    assert d["total"] == dt.total


def test_roll_expression_complex():
    rng = SeededRNG(42)
    dt1 = DiceTerm(count=2, faces=6)
    dt2 = DiceTerm(count=1, faces=4)
    children = [
        dt1,
        OperatorTerm(operator="+"),
        dt2,
        OperatorTerm(operator="+"),
        NumericTerm(value=3),
    ]
    re = RollExpression(expression="2d6+1d4+3", children=children)
    re.evaluate(rng)
    assert re.total == dt1.total + dt2.total + 3


def test_roll_expression_deterministic():
    def build() -> RollExpression:
        dt = DiceTerm(count=4, faces=6, modifier_strings=["dl1"])
        return RollExpression(expression="4d6dl1", children=[dt])

    re1 = build()
    re2 = build()
    re1.evaluate(SeededRNG(123))
    re2.evaluate(SeededRNG(123))
    assert re1.total == re2.total
    assert re1.to_dict()["total"] == re2.to_dict()["total"]


def test_full_tree_serialization():
    rng = SeededRNG(42)
    dt = DiceTerm(count=2, faces=20, modifier_strings=["kh1"], id="dice1")
    children = [
        dt,
        OperatorTerm(operator="+", id="plus1"),
        NumericTerm(value=5, id="num1"),
    ]
    re = RollExpression(expression="2d20kh1+5", children=children, id="root")
    re.evaluate(rng)
    d = re.to_dict()

    assert d["kind"] == "roll_expression"
    assert d["children"][0]["kind"] == "dice_term"
    assert d["children"][1]["kind"] == "operator_term"
    assert d["children"][2]["kind"] == "numeric_term"

    dice_node = d["children"][0]
    kept_dice = [die for die in dice_node["dice"] if die["kept"]]
    assert len(kept_dice) == 1
    assert d["total"] == kept_dice[0]["value"] + 5
