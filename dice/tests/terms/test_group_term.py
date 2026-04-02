from dice.rng import SeededRNG
from dice.terms import DiceTerm, GroupTerm, NumericTerm


def test_group_term_kind():
    gt = GroupTerm(children=[])
    assert gt.kind == "group_term"


def test_group_term_evaluate():
    rng = SeededRNG(42)
    child1 = [DiceTerm(count=1, faces=6)]
    child2 = [DiceTerm(count=1, faces=6)]
    gt = GroupTerm(children=[child1, child2])
    gt.evaluate(rng)
    expected = child1[0].total + child2[0].total
    assert gt.total == expected


def test_group_term_keep_highest():
    rng = SeededRNG(42)
    child1 = [NumericTerm(value=3)]
    child2 = [NumericTerm(value=7)]
    child3 = [NumericTerm(value=1)]
    gt = GroupTerm(
        children=[child1, child2, child3],
        modifier_strings=["kh1"],
    )
    gt.evaluate(rng)
    assert gt.total == 7


def test_group_term_keep_lowest():
    rng = SeededRNG(42)
    child1 = [NumericTerm(value=3)]
    child2 = [NumericTerm(value=7)]
    child3 = [NumericTerm(value=1)]
    gt = GroupTerm(
        children=[child1, child2, child3],
        modifier_strings=["kl1"],
    )
    gt.evaluate(rng)
    assert gt.total == 1


def test_group_term_drop_highest():
    rng = SeededRNG(42)
    child1 = [NumericTerm(value=3)]
    child2 = [NumericTerm(value=7)]
    child3 = [NumericTerm(value=1)]
    gt = GroupTerm(
        children=[child1, child2, child3],
        modifier_strings=["dh1"],
    )
    gt.evaluate(rng)
    assert gt.total == 4  # 3 + 1


def test_group_term_to_dict():
    rng = SeededRNG(42)
    child1 = [NumericTerm(value=5, id="n1")]
    child2 = [NumericTerm(value=3, id="n2")]
    gt = GroupTerm(children=[child1, child2], id="grp1")
    gt.evaluate(rng)
    d = gt.to_dict()
    assert d["id"] == "grp1"
    assert d["kind"] == "group_term"
    assert len(d["children"]) == 2
    assert d["children"][0]["total"] == 5
    assert d["children"][0]["kept"] is True
    assert d["total"] == 8
