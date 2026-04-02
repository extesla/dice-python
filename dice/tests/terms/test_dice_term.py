from dice.rng import SeededRNG
from dice.terms import DiceTerm


def test_dice_term_kind():
    dt = DiceTerm(count=2, faces=6)
    assert dt.kind == "dice_term"


def test_dice_term_notation():
    dt = DiceTerm(count=2, faces=20)
    assert dt.notation == "2d20"


def test_dice_term_notation_with_modifiers():
    dt = DiceTerm(count=2, faces=20, modifier_strings=["kh1"])
    assert dt.notation == "2d20kh1"


def test_dice_term_evaluate_populates_results():
    rng = SeededRNG(42)
    dt = DiceTerm(count=3, faces=6)
    dt.evaluate(rng)
    assert len(dt.results) == 3
    for r in dt.results:
        assert 1 <= r.value <= 6


def test_dice_term_evaluate_deterministic():
    dt1 = DiceTerm(count=4, faces=20)
    dt2 = DiceTerm(count=4, faces=20)
    dt1.evaluate(SeededRNG(99))
    dt2.evaluate(SeededRNG(99))
    assert [r.value for r in dt1.results] == [r.value for r in dt2.results]


def test_dice_term_total_sums_kept():
    rng = SeededRNG(42)
    dt = DiceTerm(count=3, faces=6)
    dt.evaluate(rng)
    expected = sum(r.value for r in dt.results if r.kept)
    assert dt.total == expected


def test_dice_term_keep_highest():
    rng = SeededRNG(42)
    dt = DiceTerm(count=4, faces=20, modifier_strings=["kh1"])
    dt.evaluate(rng)
    assert len(dt.results) == 4
    kept = [r for r in dt.results if r.kept]
    assert len(kept) == 1
    assert kept[0].value == max(r.value for r in dt.results)


def test_dice_term_keep_lowest():
    rng = SeededRNG(42)
    dt = DiceTerm(count=4, faces=20, modifier_strings=["kl1"])
    dt.evaluate(rng)
    kept = [r for r in dt.results if r.kept]
    assert len(kept) == 1
    assert kept[0].value == min(r.value for r in dt.results)


def test_dice_term_drop_highest():
    rng = SeededRNG(42)
    dt = DiceTerm(count=4, faces=20, modifier_strings=["dh1"])
    dt.evaluate(rng)
    kept = [r for r in dt.results if r.kept]
    assert len(kept) == 3
    max_val = max(r.value for r in dt.results)
    dropped = [r for r in dt.results if not r.kept]
    assert dropped[0].value == max_val


def test_dice_term_drop_lowest():
    rng = SeededRNG(42)
    dt = DiceTerm(count=4, faces=20, modifier_strings=["dl1"])
    dt.evaluate(rng)
    kept = [r for r in dt.results if r.kept]
    assert len(kept) == 3
    min_val = min(r.value for r in dt.results)
    dropped = [r for r in dt.results if not r.kept]
    assert dropped[0].value == min_val


def test_dice_term_to_dict():
    rng = SeededRNG(42)
    dt = DiceTerm(count=2, faces=6, id="test1234")
    dt.evaluate(rng)
    d = dt.to_dict()
    assert d["id"] == "test1234"
    assert d["kind"] == "dice_term"
    assert d["notation"] == "2d6"
    assert len(d["dice"]) == 2
    assert d["total"] == dt.total


def test_dice_term_to_dict_with_modifier():
    rng = SeededRNG(42)
    dt = DiceTerm(count=2, faces=20, modifier_strings=["kh1"], id="abc")
    dt.evaluate(rng)
    d = dt.to_dict()
    assert d["notation"] == "2d20kh1"
    kept_dice = [die for die in d["dice"] if die["kept"]]
    assert len(kept_dice) == 1


def test_dice_term_single_die():
    rng = SeededRNG(0)
    dt = DiceTerm(count=1, faces=20)
    dt.evaluate(rng)
    assert len(dt.results) == 1
    assert dt.total == dt.results[0].value
