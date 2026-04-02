from dice.grammar import parse


def test_parse_kh():
    r = parse("4d6kh3")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.kind == "dice_term"
    assert dt.modifier_strings == ["kh3"]


def test_parse_kl():
    r = parse("2d20kl1")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["kl1"]


def test_parse_dl():
    r = parse("4d6dl1")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["dl1"]


def test_parse_dh():
    r = parse("4d6dh1")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["dh1"]


def test_parse_explode():
    r = parse("2d6!")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["!"]


def test_parse_explode_compare():
    r = parse("2d6!>4")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["!>4"]


def test_parse_reroll():
    r = parse("2d6r<2")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["r<2"]


def test_parse_reroll_once():
    r = parse("2d6ro=1")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["ro=1"]


def test_parse_multiple_modifiers():
    r = parse("4d6r=1kh3")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["r=1", "kh3"]


def test_parse_keep_shorthand():
    r = parse("4d6k3")
    assert len(r.errors) == 0
    dt = r.ast.children[0]
    assert dt.modifier_strings == ["k3"]


def test_parse_modifier_with_arithmetic():
    r = parse("2d20kh1+7")
    assert len(r.errors) == 0
    children = r.ast.children
    assert children[0].kind == "dice_term"
    assert children[0].modifier_strings == ["kh1"]
    assert children[1].kind == "operator_term"
    assert children[2].kind == "numeric_term"
