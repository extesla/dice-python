from dice.evaluation.default import DefaultEvaluator


def test_returns_primary_total():
    ev = DefaultEvaluator()
    result = ev.evaluate({"total": 15, "kind": "roll_expression"})
    assert result["primary_total"] == 15


def test_returns_outcome_none():
    ev = DefaultEvaluator()
    result = ev.evaluate({"total": 10, "kind": "roll_expression"})
    assert result["outcome"] is None


def test_missing_total_defaults_to_zero():
    ev = DefaultEvaluator()
    result = ev.evaluate({"kind": "roll_expression"})
    assert result["primary_total"] == 0


def test_ignores_template_and_context():
    ev = DefaultEvaluator()
    result = ev.evaluate(
        {"total": 7, "kind": "roll_expression"},
        template="attack",
        context={"target_dc": 15},
    )
    assert result["primary_total"] == 7
    assert result["outcome"] is None


def test_works_with_nested_tree():
    tree = {
        "kind": "roll_expression",
        "total": 22,
        "children": [
            {"kind": "dice_term", "total": 17, "dice": [{"value": 17, "kept": True}]},
            {"kind": "operator_term", "operator": "+"},
            {"kind": "numeric_term", "value": 5},
        ],
    }
    ev = DefaultEvaluator()
    result = ev.evaluate(tree)
    assert result["primary_total"] == 22
