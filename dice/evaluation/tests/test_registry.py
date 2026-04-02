from dice.evaluation import get_evaluator, register_evaluator
from dice.evaluation.default import DefaultEvaluator


def test_default_evaluator_when_no_system():
    ev = get_evaluator(None)
    assert isinstance(ev, DefaultEvaluator)


def test_default_evaluator_for_unknown_system():
    ev = get_evaluator("unknown_system_xyz")
    assert isinstance(ev, DefaultEvaluator)


def test_registered_evaluator_returned():
    class MockEvaluator:
        def evaluate(self, execution_tree, template=None, context=None):
            return {"primary_total": 0, "outcome": "mock"}

    register_evaluator("test_system_reg", MockEvaluator())
    ev = get_evaluator("test_system_reg")
    assert not isinstance(ev, DefaultEvaluator)
    result = ev.evaluate({"total": 5})
    assert result["outcome"] == "mock"


def test_evaluate_convenience_delegates():
    from dice.evaluation import evaluate

    class SimpleEvaluator:
        def evaluate(self, execution_tree, template=None, context=None):
            return {"primary_total": execution_tree["total"], "outcome": "simple"}

    register_evaluator("test_simple", SimpleEvaluator())
    result = evaluate({"total": 10, "kind": "roll_expression"}, system="test_simple")
    assert result["outcome"] == "simple"
    assert result["primary_total"] == 10
