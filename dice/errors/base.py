from dataclasses import dataclass


@dataclass
class DiceError(Exception):
    code: str
    message: str
    position: int | None = None
    expression: str | None = None

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"


class DiceParseError(DiceError):
    """Raised when a dice expression cannot be parsed."""

    pass


class DiceExecutionError(DiceError):
    """Raised when execution fails (e.g., safety limit exceeded)."""

    pass


class DiceValidationError(DiceError):
    """Raised when a compiled AST fails validation."""

    pass
