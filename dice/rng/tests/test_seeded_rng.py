from dice.rng import SeededRNG


def test_seeded_rng_is_deterministic():
    rng1 = SeededRNG(42)
    rng2 = SeededRNG(42)
    results1 = [rng1.randint(1, 20) for _ in range(10)]
    results2 = [rng2.randint(1, 20) for _ in range(10)]
    assert results1 == results2


def test_seeded_rng_within_bounds():
    rng = SeededRNG(123)
    for _ in range(100):
        result = rng.randint(1, 6)
        assert 1 <= result <= 6


def test_different_seeds_produce_different_results():
    rng1 = SeededRNG(1)
    rng2 = SeededRNG(2)
    results1 = [rng1.randint(1, 100) for _ in range(20)]
    results2 = [rng2.randint(1, 100) for _ in range(20)]
    assert results1 != results2
