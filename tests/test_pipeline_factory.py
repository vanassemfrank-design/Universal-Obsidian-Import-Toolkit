from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport
from unobit.models import Note


def test_pipeline_factory_creates_default_pipeline():
    pipeline = PipelineFactory.create_default()

    assert pipeline is not None
    assert len(pipeline.steps) > 0


def test_pipeline_factory_default_pipeline_keeps_valid_notes():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    pipeline = PipelineFactory.create_default()

    notes = [
        Note(title="Valid", source="test", body="Content"),
    ]

    result = pipeline.run(notes, context)

    assert result == notes
    assert report.errors == []


def test_pipeline_factory_default_pipeline_cleans_title():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    pipeline = PipelineFactory.create_default()

    notes = [
        Note(title="  Title  ", source="test", body="Content"),
    ]

    result = pipeline.run(notes, context)

    assert result[0].title == "Title"


def test_pipeline_factory_default_pipeline_cleans_body():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    pipeline = PipelineFactory.create_default()

    notes = [
        Note(title="Title", source="test", body="\n\nContent\n\n"),
    ]

    result = pipeline.run(notes, context)

    assert result[0].body == "Content"