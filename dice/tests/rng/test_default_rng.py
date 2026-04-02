from dice.rng import DefaultRNG


def test_default_rng_returns_int():
    rng = DefaultRNG()
    result = rng.randint(1, 6)
    assert isinstance(result, int)


def test_default_rng_within_bounds():
    rng = DefaultRNG()
    for _ in range(100):
        result = rng.randint(1, 6)
        assert 1 <= result <= 6


def test_default_rng_single_value():
    rng = DefaultRNG()
    result = rng.randint(5, 5)
    assert result == 5
