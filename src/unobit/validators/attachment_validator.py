from unobit.validators.base import ValidationMessage, ValidationResult


class AttachmentValidator:
    def validate(self, item: object) -> ValidationResult:
        messages: list[ValidationMessage] = []

        attachments = getattr(item, "attachments", None)

        if attachments is None:
            return ValidationResult(messages=[])

        for attachment in attachments:
            filename = getattr(attachment, "filename", None)

            if not filename or not str(filename).strip():
                messages.append(
                    ValidationMessage(
                        level="warning",
                        code="attachment-missing-filename",
                        message="Attachment has no filename",
                    )
                )

        return ValidationResult(messages=messages)