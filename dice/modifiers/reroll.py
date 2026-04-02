from __future__ import annotations

from dice.constants import MAX_EXPLOSIONS
from dice.modifiers.base import ModifierFn, ModifierSpec, matches_compare_point
from dice.rng import RNG, roll_die
from dice.terms.die_result import DieResult


def _reroll(
    results: list[DieResult],
    spec: ModifierSpec,
    rng: RNG,
    faces: int,
    *,
    once: bool,
) -> list[DieResult]:
    """Shared implementation for reroll and reroll-once."""
    iterations = 0
    to_check = [
        r for r in results
        if matches_compare_point(r.value, spec.compare_point, faces)
    ]
    while to_check:
        next_round: list[DieResult] = []
        for die in to_check:
            iterations += 1
            if iterations > MAX_EXPLOSIONS:
                # Safety valve — prevent infinite reroll loops
                break
            die.rerolled = True
            die.kept = False
            replacement = DieResult(value=roll_die(faces, rng))
            results.append(replacement)
            if (
                not once
                and matches_compare_point(replacement.value, spec.compare_point, faces)
            ):
                next_round.append(replacement)
        if iterations > MAX_EXPLOSIONS:
            break
        to_check = next_round
    return results


def reroll(
    results: list[DieResult], spec: ModifierSpec, rng: RNG, faces: int
) -> list[DieResult]:
    """Reroll dice matching the compare point until none match."""
    return _reroll(results, spec, rng, faces, once=False)


def reroll_once(
    results: list[DieResult], spec: ModifierSpec, rng: RNG, faces: int
) -> list[DieResult]:
    """Reroll dice matching the compare point at most once."""
    return _reroll(results, spec, rng, faces, once=True)


REROLL_MODIFIERS: dict[str, ModifierFn] = {
    "r": reroll,
    "ro": reroll_once,
}
