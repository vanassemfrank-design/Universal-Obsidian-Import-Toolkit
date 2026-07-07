from unobit.validators.base import ValidationMessage, ValidationResult


class NoteValidator:
    def validate(self, item) -> ValidationResult:
        messages: list[ValidationMessage] = []

        title = getattr(item, "title", None)
        content = getattr(item, "content", None)

        if not title or not str(title).strip():
            messages.append(
                ValidationMessage(
                    level="warning",
                    code="note-missing-title",
                    message="Note has no title",
                )
            )

        if content is None:
            messages.append(
                ValidationMessage(
                    level="error",
                    code="note-missing-content",
                    message="Note has no content",
                )
            )

        return ValidationResult(messages=messages)