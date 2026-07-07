from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class ValidationMessage:
    level: str
    code: str
    message: str
    context: dict[str, Any] | None = None


@dataclass
class ValidationResult:
    messages: list[ValidationMessage]

    @property
    def has_errors(self) -> bool:
        return any(message.level == "error" for message in self.messages)

    @property
    def has_warnings(self) -> bool:
        return any(message.level == "warning" for message in self.messages)


class Validator(Protocol):
    def validate(self, item: object) -> ValidationResult:
        ...