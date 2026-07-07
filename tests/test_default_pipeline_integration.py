from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport


class FakeAttachment:
    def __init__(self, filename):
        self.filename = filename


class FakeNote:
    def __init__(self, title, content, attachments=None, metadata=None):
        self.title = title
        self.content = content
        self.attachments = attachments or []
        self.metadata = metadata


def test_default_pipeline_validates_and_processes_notes():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    notes = [
        FakeNote(
            title="  Geldige notitie  ",
            content="\n\nInhoud\n\n",
            attachments=[
                FakeAttachment(filename="image.png"),
            ],
            metadata={"guid": "abc"},
        ),
        FakeNote(
            title="",
            content=None,
            attachments=[
                FakeAttachment(filename=""),
            ],
            metadata=None,
        ),
    ]

    pipeline = PipelineFactory.create_default()

    result = pipeline.run(notes, context)

    assert len(result) == 2

    assert result[0].title == "Geldige notitie"
    assert result[0].content == "Inhoud"

    codes = [
        message.context["code"]
        for message in report.warnings + report.errors
    ]

    assert "note-missing-title" in codes
    assert "note-missing-content" in codes
    assert "attachment-missing-filename" in codes
    assert "note-missing-metadata" in codes