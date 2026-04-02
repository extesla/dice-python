import random


class DefaultRNG:
    """RNG backed by the system's cryptographic random source."""

    def __init__(self) -> None:
        self._rng = random.SystemRandom()

    def randint(self, a: int, b: int) -> int:
        return self._rng.randint(a, b)
