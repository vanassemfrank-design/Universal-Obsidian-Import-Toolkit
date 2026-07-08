from unobit.validators.base import ValidationMessage, ValidationResult


class NoteValidator:
    def validate(self, item) -> ValidationResult:
        messages: list[ValidationMessage] = []

        title = getattr(item, "title", None)
        body = getattr(item, "body", None)

        if not title or not str(title).strip():
            messages.append(
                ValidationMessage(
                    level="warning",
                    code="note-missing-title",
                    message="Note has no title",
                )
            )

        if body is None:
            messages.append(
                ValidationMessage(
                    level="error",
                    code="note-missing-body",
                    message="Note has no body",
                )
            )

        return ValidationResult(messages=messages)