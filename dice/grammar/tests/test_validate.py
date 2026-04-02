from dice.grammar import validate


def test_validate_valid_expression():
    errors = validate("2d6+3")
    assert errors == []


def test_validate_complex_valid():
    errors = validate("4d6kh3+2d4+5")
    assert errors == []


def test_validate_invalid_expression():
    errors = validate("xyz")
    assert len(errors) >= 1


def test_validate_empty():
    errors = validate("")
    assert len(errors) == 1
    assert errors[0].code == "EMPTY_EXPRESSION"


def test_validate_returns_list():
    result = validate("1d20")
    assert isinstance(result, list)
