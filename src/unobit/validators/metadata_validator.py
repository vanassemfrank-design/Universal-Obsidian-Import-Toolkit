from unobit.validators.base import ValidationMessage, ValidationResult


class MetadataValidator:
    def validate(self, item: object) -> ValidationResult:
        messages: list[ValidationMessage] = []

        metadata = getattr(item, "metadata", None)

        if metadata is None:
            messages.append(
                ValidationMessage(
                    level="warning",
                    code="note-missing-metadata",
                    message="Note has no metadata",
                )
            )

        return ValidationResult(messages=messages)