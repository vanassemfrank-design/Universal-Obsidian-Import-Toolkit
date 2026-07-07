from unobit.validators.base import ValidationMessage, ValidationResult


def test_validation_result_detects_errors_and_warnings():
    result = ValidationResult(
        messages=[
            ValidationMessage(
                level="warning",
                code="missing-title",
                message="Note has no title",
            ),
            ValidationMessage(
                level="error",
                code="missing-content",
                message="Note has no content",
            ),
        ]
    )

    assert result.has_warnings is True
    assert result.has_errors is True