from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.report import ImportReport
from unobit.models import Note
from unobit.processors.evernote_internal_link_processor import (
    EvernoteInternalLinkProcessor,
)


def test_evernote_internal_link_processor_replaces_known_link():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    target_guid = "11111111-1111-1111-1111-111111111111"

    source = Note(
        title="Source Note",
        source="evernote",
        body=f"Zie [deze notitie](evernote:///view/123/abc/{target_guid}/{target_guid}/).",
        metadata={"guid": "22222222-2222-2222-2222-222222222222"},
    )

    target = Note(
        title="Target Note",
        source="evernote",
        body="Ik ben het doel.",
        metadata={"guid": target_guid},
    )

    processor = EvernoteInternalLinkProcessor()
    result = processor.process_all([source, target], context)

    assert "[[Target Note|deze notitie]]" in result[0].body
    assert len(report.warnings) == 0


def test_evernote_internal_link_processor_keeps_unknown_link_and_warns():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    unknown_guid = "99999999-9999-9999-9999-999999999999"

    source = Note(
        title="Source Note",
        source="evernote",
        body=f"Zie [missing](evernote:///view/123/abc/{unknown_guid}/{unknown_guid}/).",
        metadata={"guid": "22222222-2222-2222-2222-222222222222"},
    )

    processor = EvernoteInternalLinkProcessor()
    result = processor.process_all([source], context)

    assert "evernote:///view/" in result[0].body
    assert len(report.warnings) == 1
    assert report.warnings[0].context["code"] == "evernote-link-unresolved"