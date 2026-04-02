import random


class SeededRNG:
    """Deterministic RNG for testing. Seeded with a fixed value."""

    def __init__(self, seed: int) -> None:
        self._rng = random.Random(seed)

    def randint(self, a: int, b: int) -> int:
        return self._rng.randint(a, b)
