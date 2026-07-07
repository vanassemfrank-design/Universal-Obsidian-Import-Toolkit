from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ImportMessage:
    level: str
    message: str
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class ImportReport:
    source: str
    importer: str
    started_at: datetime = field(default_factory=datetime.now)
    finished_at: datetime | None = None

    notes_total: int = 0
    notes_success: int = 0
    notes_failed: int = 0

    attachments_total: int = 0
    attachments_exported: int = 0
    attachments_failed: int = 0

    warnings: list[ImportMessage] = field(default_factory=list)
    errors: list[ImportMessage] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    def finish(self) -> None:
        self.finished_at = datetime.now()

    def add_warning(self, message: str, **context: Any) -> None:
        self.warnings.append(
            ImportMessage(level="warning", message=message, context=context)
        )

    def add_error(self, message: str, **context: Any) -> None:
        self.errors.append(
            ImportMessage(level="error", message=message, context=context)
        )