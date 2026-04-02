import pytest

from dice.modifiers.parser import parse_modifier_string


def test_parse_kh():
    specs = parse_modifier_string("kh3")
    assert len(specs) == 1
    assert specs[0].key == "kh"
    assert specs[0].argument == 3


def test_parse_kh_default():
    specs = parse_modifier_string("kh")
    assert len(specs) == 1
    assert specs[0].key == "kh"
    assert specs[0].argument is None


def test_parse_dl():
    specs = parse_modifier_string("dl1")
    assert len(specs) == 1
    assert specs[0].key == "dl"
    assert specs[0].argument == 1


def test_parse_explode():
    specs = parse_modifier_string("!")
    assert len(specs) == 1
    assert specs[0].key == "!"
    assert specs[0].argument is None
    assert specs[0].compare_point is None


def test_parse_explode_with_compare():
    specs = parse_modifier_string("!>=5")
    assert len(specs) == 1
    assert specs[0].key == "!"
    assert specs[0].compare_point == ">=5"


def test_parse_reroll_with_compare():
    specs = parse_modifier_string("r<2")
    assert len(specs) == 1
    assert specs[0].key == "r"
    assert specs[0].compare_point == "<2"


def test_parse_reroll_once():
    specs = parse_modifier_string("ro=1")
    assert len(specs) == 1
    assert specs[0].key == "ro"
    assert specs[0].compare_point == "=1"


def test_parse_compound():
    specs = parse_modifier_string("!!")
    assert len(specs) == 1
    assert specs[0].key == "!!"


def test_parse_penetrate():
    specs = parse_modifier_string("!p")
    assert len(specs) == 1
    assert specs[0].key == "!p"


def test_parse_multiple_modifiers():
    specs = parse_modifier_string("kh3r<2!")
    assert len(specs) == 3
    assert specs[0].key == "kh"
    assert specs[0].argument == 3
    assert specs[1].key == "r"
    assert specs[1].compare_point == "<2"
    assert specs[2].key == "!"


def test_parse_complex_string():
    specs = parse_modifier_string("r=1kh3!")
    assert len(specs) == 3
    keys = [s.key for s in specs]
    assert keys == ["r", "kh", "!"]


def test_parse_sort():
    specs = parse_modifier_string("sa")
    assert len(specs) == 1
    assert specs[0].key == "sa"


def test_parse_min_max():
    specs = parse_modifier_string("min2")
    assert len(specs) == 1
    assert specs[0].key == "min"
    assert specs[0].argument == 2


def test_parse_empty_string():
    specs = parse_modifier_string("")
    assert specs == []


def test_parse_invalid_raises():
    with pytest.raises(ValueError, match="Unrecognized modifier"):
        parse_modifier_string("zz")
