from dice.grammar import parse


def test_parse_d_percent():
    r = parse("d%")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.kind == "dice_term"
    assert dt.faces == 100
    assert dt.count == 1


def test_parse_1d_percent():
    r = parse("1d%")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.faces == 100
    assert dt.count == 1
