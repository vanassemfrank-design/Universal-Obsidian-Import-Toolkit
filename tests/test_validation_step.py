from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.report import ImportReport
from unobit.core.validation_step import ValidationStep
from unobit.validators.base import ValidationMessage, ValidationResult


class FakeWarningValidator:
    def validate(self, item):
        return ValidationResult(
            messages=[
                ValidationMessage(
                    level="warning",
                    code="fake-warning",
                    message="Fake warning",
                    context={"item": item},
                )
            ]
        )


class FakeErrorValidator:
    def validate(self, item):
        return ValidationResult(
            messages=[
                ValidationMessage(
                    level="error",
                    code="fake-error",
                    message="Fake error",
                    context={"item": item},
                )
            ]
        )


def test_validation_step_adds_messages_to_report():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    step = ValidationStep(
        validators=[
            FakeWarningValidator(),
            FakeErrorValidator(),
        ]
    )

    result = list(step.run(["note-1"], context))

    assert result == ["note-1"]
    assert len(report.warnings) == 1
    assert len(report.errors) == 1
    assert report.warnings[0].context["code"] == "fake-warning"
    assert report.errors[0].context["code"] == "fake-error"