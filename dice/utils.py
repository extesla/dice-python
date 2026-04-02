import logging
import random

#: Module logger
logger = logging.getLogger(__name__)


def classname(obj: object) -> str:
    """Returns the name of an objects class"""
    return obj.__class__.__name__


def mt_rand(min: int | None, max: int | None) -> int:
    """
    Mersenne Twist pseudo random number generator (PRNG) that has value-safe
    operations for the minimum value.

    :param min: the lower boundary of the random number range.
    :type min: int
    :param max: the upper boundary of the random number range.
    :type max: int
    """
    if min is None:
        logger.warning("Minimum value not specified, assuming minimum value of 1")
        min = 1
    if max is None:
        raise TypeError("Random requires a maximum boundary. Given: None")
    return random.randint(min, max)


def to_int(obj: object, default: int = 0) -> int:
    """
    Value-safe conversion of an object to an ``int``. If the ``obj`` being
    converted is either ``None`` or an empty string, the object will be
    assigned the value of ``default``.

    :param obj: the object being cast as an integer.
    :param default: the default value to
    """
    try:
        return int(obj)  # type: ignore[call-overload]
    except (TypeError, ValueError):
        return int(default)
