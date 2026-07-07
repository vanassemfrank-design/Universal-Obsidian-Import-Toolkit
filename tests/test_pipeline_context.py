from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.report import ImportReport


def test_pipeline_context_holds_paths_and_report():
    report = ImportReport(
        source="samples/evernote/test.enex",
        importer="evernote",
    )

    context = PipelineContext(
        source_path=Path("samples/evernote/test.enex"),
        output_path=Path("output/evernote"),
        importer_name="evernote",
        report=report,
    )

    assert context.importer_name == "evernote"
    assert context.source_path.name == "test.enex"
    assert context.output_path.name == "evernote"
    assert context.report is report