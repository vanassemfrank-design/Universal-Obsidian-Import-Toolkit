from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.report import ImportReport
from unobit.models import Note
from unobit.resolvers.evernote_links import EvernoteInternalLinkResolver


def test_evernote_internal_link_resolver_replaces_known_link():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    target_guid = "22222222-2222-2222-2222-222222222222"

    source = Note(
        title="Shopping List",
        source="evernote",
        body=f"See [Recipe](evernote:///view/12345/s1/{target_guid}/{target_guid}/)",
        metadata={"guid": "11111111-1111-1111-1111-111111111111"},
    )

    target = Note(
        title="Recipe",
        source="evernote",
        body="Ingredients...",
        metadata={"guid": target_guid},
    )

    resolver = EvernoteInternalLinkResolver()
    result = resolver.resolve([source, target], context)

    assert "[[Recipe]]" in result[0].body
    assert len(report.warnings) == 0


def test_evernote_internal_link_resolver_warns_on_unknown_link():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    unknown_guid = "99999999-9999-9999-9999-999999999999"

    source = Note(
        title="Broken Link Source",
        source="evernote",
        body=f"See [Missing](evernote:///view/12345/s1/{unknown_guid}/{unknown_guid}/)",
        metadata={"guid": "11111111-1111-1111-1111-111111111111"},
    )

    resolver = EvernoteInternalLinkResolver()
    result = resolver.resolve([source], context)

    assert "evernote:///view/" in result[0].body
    assert len(report.warnings) == 1
    assert report.warnings[0].context["code"] == "evernote-link-unresolved"