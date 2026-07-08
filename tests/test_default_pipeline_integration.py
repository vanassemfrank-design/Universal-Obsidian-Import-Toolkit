from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport
from unobit.models import Attachment, Note


def test_default_pipeline_validates_and_processes_notes():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    notes = [
        Note(
            title="  Geldige notitie  ",
            source="evernote",
            body="\n\nInhoud\n\n",
            attachments=[
                Attachment(filename="image.png"),
            ],
            metadata={"guid": "abc"},
        ),
        Note(
            title="",
            source="evernote",
            body=None,
            attachments=[
                Attachment(filename=""),
            ],
            metadata=None,
        ),
    ]

    pipeline = PipelineFactory.create_default()

    result = pipeline.run(notes, context)

    assert len(result) == 2

    assert result[0].title == "Geldige notitie"
    assert result[0].body == "Inhoud"

    assert len(report.warnings) == 3
    assert len(report.errors) == 1