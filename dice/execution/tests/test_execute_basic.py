from dice import roll
from dice.rng import SeededRNG


def test_execute_1d6():
    result = roll("1d6", rng=SeededRNG(42))
    assert isinstance(result.total, (int, float))
    assert 1 <= result.total <= 6


def test_execute_2d20_plus_5():
    result = roll("2d20+5", rng=SeededRNG(42))
    tree = result.tree
    assert tree["kind"] == "roll_expression"
    assert len(tree["children"]) == 3
    assert tree["children"][0]["kind"] == "dice_term"
    assert tree["children"][1]["kind"] == "operator_term"
    assert tree["children"][2]["kind"] == "numeric_term"


def test_execute_subtraction():
    result = roll("3d8-2", rng=SeededRNG(42))
    tree = result.tree
    assert tree["total"] == result.total
    assert tree["children"][1]["operator"] == "-"


def test_execute_multiplication():
    result = roll("1d20*2", rng=SeededRNG(42))
    tree = result.tree
    assert tree["total"] == result.total


def test_execute_deterministic():
    r1 = roll("2d6+3", rng=SeededRNG(99))
    r2 = roll("2d6+3", rng=SeededRNG(99))
    assert r1.total == r2.total
    # Trees differ in auto-generated IDs but dice values match
    d1 = r1.tree["children"][0]["dice"]
    d2 = r2.tree["children"][0]["dice"]
    assert [d["value"] for d in d1] == [d["value"] for d in d2]


def test_execute_expression_preserved():
    result = roll("1d6", rng=SeededRNG(42))
    assert result.expression == "1d6"


def test_execute_syntax_version():
    result = roll("1d6", rng=SeededRNG(42))
    assert result.syntax_version == "1.0"
