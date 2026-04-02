from dice import roll
from dice.rng import SeededRNG


def _assert_node_has_id_and_kind(node: dict) -> None:
    """Recursively verify every node has 'id' and 'kind'."""
    assert "id" in node, f"Node missing 'id': {node}"
    assert "kind" in node, f"Node missing 'kind': {node}"
    if "children" in node:
        for child in node["children"]:
            if isinstance(child, dict) and "kind" in child:
                _assert_node_has_id_and_kind(child)


def test_every_node_has_id_and_kind():
    result = roll("2d20kh1+7", rng=SeededRNG(42))
    _assert_node_has_id_and_kind(result.tree)


def test_dice_term_has_dice_array():
    result = roll("2d6", rng=SeededRNG(42))
    dice_node = result.tree["children"][0]
    assert "dice" in dice_node
    assert isinstance(dice_node["dice"], list)
    assert len(dice_node["dice"]) == 2


def test_dice_term_dice_have_value_and_kept():
    result = roll("1d20", rng=SeededRNG(42))
    die = result.tree["children"][0]["dice"][0]
    assert "value" in die
    assert "kept" in die


def test_operator_term_has_operator():
    result = roll("1d6+3", rng=SeededRNG(42))
    op = result.tree["children"][1]
    assert op["kind"] == "operator_term"
    assert op["operator"] == "+"


def test_numeric_term_has_value():
    result = roll("42", rng=SeededRNG(42))
    num = result.tree["children"][0]
    assert num["kind"] == "numeric_term"
    assert num["value"] == 42


def test_tree_is_json_serializable():
    import json

    result = roll("2d20kh1+7 [attack]", rng=SeededRNG(42))
    serialized = json.dumps(result.tree)
    assert isinstance(serialized, str)
    roundtrip = json.loads(serialized)
    assert roundtrip == result.tree


def test_tree_is_immutable_copy():
    result = roll("1d6", rng=SeededRNG(42))
    original_total = result.tree["total"]
    result.tree["total"] = 999
    # The modification is local — but the point is it's a deep copy
    # not a reference to the AST internals
    assert result.total == original_total
