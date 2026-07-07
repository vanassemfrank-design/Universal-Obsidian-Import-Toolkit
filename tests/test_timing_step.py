from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.report import ImportReport
from unobit.core.timing_step import TimingStep


def test_timing_step_adds_timing_to_report():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    step = TimingStep(name="validation")

    result = list(step.run(["note-1", "note-2"], context))

    assert result == ["note-1", "note-2"]
    assert "validation" in report.timings
    assert report.timings["validation"] >= 0