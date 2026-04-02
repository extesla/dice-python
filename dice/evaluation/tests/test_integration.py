from typing import Any

from dice import roll
from dice.evaluation import register_evaluator
from dice.rng import SeededRNG


class TestDnDEvaluator:
    def evaluate(
        self,
        execution_tree: dict[str, Any],
        template: str | None = None,
        context: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        total = execution_tree.get("total", 0)
        dc = (context or {}).get("target_dc")
        outcome = None
        if dc is not None:
            outcome = "success" if total >= dc else "failure"
        return {"primary_total": total, "outcome": outcome}


def test_full_pipeline_with_evaluator():
    register_evaluator("test_dnd_integ", TestDnDEvaluator())
    result = roll(
        "1d20+5",
        rng=SeededRNG(42),
        system="test_dnd_integ",
        context={"target_dc": 15},
    )
    assert result.execution is not None
    assert result.evaluation is not None
    assert result.evaluation["primary_total"] == result.total
    assert result.evaluation["outcome"] in ("success", "failure")


def test_full_pipeline_without_evaluator():
    result = roll("1d20+5", rng=SeededRNG(42))
    assert result.execution is not None
    assert result.evaluation is None
    assert isinstance(result.total, (int, float))


def test_full_pipeline_with_template():
    register_evaluator("test_dnd_tmpl", TestDnDEvaluator())
    result = roll(
        "1d20+5",
        rng=SeededRNG(42),
        system="test_dnd_tmpl",
        template="attack",
        context={"target_dc": 10},
    )
    assert result.evaluation is not None
    assert result.evaluation["outcome"] in ("success", "failure")
