from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport
from unobit.models import Note


def test_default_pipeline_adds_timings():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    notes = [
        Note(title="Title", source="test", body="Content"),
    ]

    pipeline = PipelineFactory.create_default()
    pipeline.run(notes, context)

    assert "validation" in report.timings
    assert "processing" in report.timings
    assert report.timings["validation"] >= 0
    assert report.timings["processing"] >= 0