from dice import roll
from dice.rng import SeededRNG


def test_execute_keep_highest():
    result = roll("4d6kh3", rng=SeededRNG(42))
    tree = result.tree
    dice_node = tree["children"][0]
    assert dice_node["kind"] == "dice_term"
    assert len(dice_node["dice"]) == 4
    kept = [d for d in dice_node["dice"] if d["kept"]]
    assert len(kept) == 3


def test_execute_keep_lowest():
    result = roll("2d20kl1", rng=SeededRNG(42))
    tree = result.tree
    dice_node = tree["children"][0]
    kept = [d for d in dice_node["dice"] if d["kept"]]
    assert len(kept) == 1
    all_values = [d["value"] for d in dice_node["dice"]]
    assert kept[0]["value"] == min(all_values)


def test_execute_explode():
    result = roll("2d6!", rng=SeededRNG(42))
    tree = result.tree
    dice_node = tree["children"][0]
    # At least 2 dice (may have more from explosions)
    assert len(dice_node["dice"]) >= 2


def test_execute_reroll():
    result = roll("2d6r<2", rng=SeededRNG(42))
    tree = result.tree
    dice_node = tree["children"][0]
    # Check that rerolled dice are marked
    for d in dice_node["dice"]:
        if d.get("rerolled"):
            assert d["kept"] is False


def test_execute_modifier_total_correct():
    result = roll("4d6kh3", rng=SeededRNG(42))
    tree = result.tree
    dice_node = tree["children"][0]
    kept_sum = sum(d["value"] for d in dice_node["dice"] if d["kept"])
    assert dice_node["total"] == kept_sum
    assert tree["total"] == kept_sum
