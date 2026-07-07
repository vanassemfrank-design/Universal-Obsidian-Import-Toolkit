from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.pipeline import ProcessingPipeline
from unobit.core.report import ImportReport


class UppercaseStep:
    def run(self, items, context):
        for item in items:
            yield item.upper()


class PrefixStep:
    def run(self, items, context):
        for item in items:
            yield f"note-{item}"


def test_processing_pipeline_runs_steps_in_order():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    pipeline = ProcessingPipeline(
        steps=[
            UppercaseStep(),
            PrefixStep(),
        ]
    )

    result = pipeline.run(["a", "b"], context)

    assert result == ["note-A", "note-B"]

def test_processing_pipeline_with_step_returns_self():
    pipeline = ProcessingPipeline()

    returned = pipeline.with_step(UppercaseStep())

    assert returned is pipeline
    assert len(pipeline.steps) == 1