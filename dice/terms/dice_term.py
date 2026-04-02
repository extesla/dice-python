from __future__ import annotations

import re
from typing import Any

from dice.rng import RNG, roll_die
from dice.terms.base import RollTerm
from dice.terms.die_result import DieResult


_MODIFIER_RE = re.compile(r"^(kh|kl|dh|dl)(\d+)$")


def _apply_modifiers(
    results: list[DieResult], modifier_strings: list[str]
) -> list[DieResult]:
    """Apply keep/drop modifiers to die results.

    Supported modifiers:
      kh<n>  keep highest n
      kl<n>  keep lowest n
      dh<n>  drop highest n
      dl<n>  drop lowest n

    Modifiers not yet supported are silently ignored (they will be
    handled by the modifier pipeline once it is implemented).
    """
    for mod in modifier_strings:
        m = _MODIFIER_RE.match(mod)
        if m is None:
            continue
        action = m.group(1)
        n = int(m.group(2))
        indexed = sorted(
            enumerate(results), key=lambda pair: pair[1].value
        )
        if action == "kh":
            keep_indices = {i for i, _ in indexed[-n:]}
        elif action == "kl":
            keep_indices = {i for i, _ in indexed[:n]}
        elif action == "dh":
            drop_indices = {i for i, _ in indexed[-n:]}
            keep_indices = {i for i in range(len(results))} - drop_indices
        elif action == "dl":
            drop_indices = {i for i, _ in indexed[:n]}
            keep_indices = {i for i in range(len(results))} - drop_indices
        else:
            continue
        for i, r in enumerate(results):
            r.kept = i in keep_indices
    return results


class DiceTerm(RollTerm):
    """A term representing one or more dice of the same type to be rolled."""

    kind: str = "dice_term"

    def __init__(
        self,
        *,
        count: int,
        faces: int,
        modifier_strings: list[str] | None = None,
        id: str | None = None,
    ) -> None:
        super().__init__(id=id)
        self.count = count
        self.faces = faces
        self.modifier_strings: list[str] = modifier_strings or []
        self.results: list[DieResult] = []

    @property
    def notation(self) -> str:
        base = f"{self.count}d{self.faces}"
        return base + "".join(self.modifier_strings)

    @property
    def total(self) -> int:
        return sum(r.value for r in self.results if r.kept)

    def evaluate(self, rng: RNG) -> DiceTerm:
        self.results = [
            DieResult(value=roll_die(self.faces, rng))
            for _ in range(self.count)
        ]
        if self.modifier_strings:
            _apply_modifiers(self.results, self.modifier_strings)
        self._evaluated = True
        return self

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "kind": self.kind,
            "notation": self.notation,
            "dice": [r.to_dict() for r in self.results],
            "total": self.total,
        }
