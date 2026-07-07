from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport


class FakeNote:
    def __init__(self, title, content):
        self.title = title
        self.content = content


def test_pipeline_factory_creates_default_pipeline():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    pipeline = PipelineFactory.create_default()

    result = pipeline.run(
        [
            FakeNote(title="", content="Hello"),
            FakeNote(title="Valid", content="World"),
        ],
        context,
    )

    assert len(result) == 2
    assert len(report.warnings) == 1
    assert report.warnings[0].context["code"] == "note-missing-title"