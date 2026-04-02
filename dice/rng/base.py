from typing import Protocol


class RNG(Protocol):
    def randint(self, a: int, b: int) -> int:
        """Return a random integer N such that a <= N <= b."""
        ...
