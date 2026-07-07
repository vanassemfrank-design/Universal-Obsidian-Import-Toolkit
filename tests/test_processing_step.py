from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.processing_step import ProcessingStep
from unobit.core.report import ImportReport


class FakeNote:
    def __init__(self, title: str) -> None:
        self.title = title


class PrefixProcessor:
    def process(self, item):
        item.title = f"PREFIX-{item.title}"
        return item


class SuffixProcessor:
    def process(self, item):
        item.title = f"{item.title}-SUFFIX"
        return item


def test_processing_step_runs_processors_in_order():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    step = ProcessingStep(
        processors=[
            PrefixProcessor(),
            SuffixProcessor(),
        ]
    )

    result = list(step.run([FakeNote("Note")], context))

    assert result[0].title == "PREFIX-Note-SUFFIX"