from dice.grammar import parse


def test_parse_flavor_text():
    r = parse("2d20kh1+7 [attack]")
    assert len(r.errors) == 0
    assert r.ast.label == "attack"


def test_parse_flavor_text_with_spaces():
    r = parse("1d20+5 [attack roll]")
    assert len(r.errors) == 0
    assert r.ast.label == "attack roll"


def test_parse_no_flavor_text():
    r = parse("1d20+5")
    assert len(r.errors) == 0
    assert r.ast.label is None


def test_parse_flavor_does_not_affect_children():
    r = parse("1d6 [damage]")
    assert len(r.errors) == 0
    assert len(r.ast.children) == 1
    assert r.ast.children[0].kind == "dice_term"
    assert r.ast.label == "damage"
