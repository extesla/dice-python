from dice.errors import DiceParseError
from dice.grammar import parse


def test_parse_empty_string():
    r = parse("")
    assert len(r.errors) == 1
    assert r.errors[0].code == "EMPTY_EXPRESSION"


def test_parse_whitespace_only():
    r = parse("   ")
    assert len(r.errors) == 1
    assert r.errors[0].code == "EMPTY_EXPRESSION"


def test_parse_nonsense():
    r = parse("xyz")
    assert len(r.errors) == 1
    assert r.errors[0].code == "PARSE_ERROR"


def test_parse_error_is_dice_parse_error():
    r = parse("!!invalid!!")
    assert len(r.errors) >= 1
    assert isinstance(r.errors[0], DiceParseError)


def test_parse_error_has_expression():
    r = parse("bad input")
    assert r.errors[0].expression == "bad input"


def test_parse_error_returns_dummy_ast():
    r = parse("")
    assert r.ast.kind == "roll_expression"
    assert r.ast.children == []
