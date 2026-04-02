from dice.terms import DieResult


def test_die_result_defaults():
    r = DieResult(value=5)
    assert r.value == 5
    assert r.kept is True
    assert r.exploded is False
    assert r.rerolled is False
    assert r.critical is None
    assert r.matched is False


def test_to_dict_minimal():
    r = DieResult(value=3)
    d = r.to_dict()
    assert d == {"value": 3, "kept": True}


def test_to_dict_not_kept():
    r = DieResult(value=2, kept=False)
    d = r.to_dict()
    assert d == {"value": 2, "kept": False}


def test_to_dict_exploded():
    r = DieResult(value=6, exploded=True)
    d = r.to_dict()
    assert d["exploded"] is True


def test_to_dict_rerolled():
    r = DieResult(value=1, rerolled=True)
    d = r.to_dict()
    assert d["rerolled"] is True


def test_to_dict_critical_success():
    r = DieResult(value=20, critical="success")
    d = r.to_dict()
    assert d["critical"] == "success"


def test_to_dict_critical_failure():
    r = DieResult(value=1, critical="failure")
    d = r.to_dict()
    assert d["critical"] == "failure"


def test_to_dict_matched():
    r = DieResult(value=4, matched=True)
    d = r.to_dict()
    assert d["matched"] is True


def test_to_dict_all_flags():
    r = DieResult(
        value=6,
        kept=True,
        exploded=True,
        rerolled=True,
        critical="success",
        matched=True,
    )
    d = r.to_dict()
    assert d == {
        "value": 6,
        "kept": True,
        "exploded": True,
        "rerolled": True,
        "critical": "success",
        "matched": True,
    }


def test_to_dict_omits_false_flags():
    r = DieResult(value=4, exploded=False, rerolled=False, matched=False)
    d = r.to_dict()
    assert "exploded" not in d
    assert "rerolled" not in d
    assert "matched" not in d
