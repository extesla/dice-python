import pytest

from dice import roll
from dice.errors import DiceParseError
from dice.rng import SeededRNG
from dice.roll_result import RollResult


def test_roll_returns_roll_result():
    result = roll("2d20kh1+7", rng=SeededRNG(42))
    assert isinstance(result, RollResult)


def test_roll_has_tree():
    result = roll("1d6", rng=SeededRNG(42))
    assert isinstance(result.tree, dict)
    assert result.tree["kind"] == "roll_expression"


def test_roll_has_total():
    result = roll("1d6+3", rng=SeededRNG(42))
    assert isinstance(result.total, (int, float))


def test_roll_has_expression():
    result = roll("2d6", rng=SeededRNG(42))
    assert result.expression == "2d6"


def test_roll_invalid_expression_raises():
    with pytest.raises(DiceParseError):
        roll("")


def test_roll_invalid_syntax_raises():
    with pytest.raises(DiceParseError):
        roll("xyz")


def test_roll_with_flavor():
    result = roll("1d20+5 [attack]", rng=SeededRNG(42))
    assert result.tree.get("label") == "attack"


def test_roll_deterministic():
    r1 = roll("4d6kh3", rng=SeededRNG(123))
    r2 = roll("4d6kh3", rng=SeededRNG(123))
    assert r1.total == r2.total
    d1 = r1.tree["children"][0]["dice"]
    d2 = r2.tree["children"][0]["dice"]
    assert [d["value"] for d in d1] == [d["value"] for d in d2]
