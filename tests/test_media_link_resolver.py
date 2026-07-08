from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.report import ImportReport
from unobit.models import Attachment, Note
from unobit.resolvers.media_links import MediaLinkResolver


def make_context() -> PipelineContext:
    return PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=ImportReport(source="test.enex", importer="evernote"),
    )


def test_media_link_resolver_replaces_image_placeholder():
    context = make_context()

    attachment = Attachment(
        filename="image.png",
        mime_type="image/png",
        checksum="abc123",
    )

    note = Note(
        title="Note",
        source="evernote",
        body="Before [UNOBIT-MEDIA:1:image/png:abc123] After",
        attachments=[attachment],
    )

    resolver = MediaLinkResolver()
    result = resolver.resolve([note], context)

    assert "![[Attachments/image.png]]" in result[0].body
    assert context.report.media_total == 1
    assert context.report.media_resolved == 1
    assert context.report.media_unresolved == 0


def test_media_link_resolver_replaces_pdf_placeholder():
    context = make_context()

    attachment = Attachment(
        filename="document.pdf",
        mime_type="application/pdf",
        checksum="def456",
    )

    note = Note(
        title="Note",
        source="evernote",
        body="PDF [UNOBIT-MEDIA:1:application/pdf:def456]",
        attachments=[attachment],
    )

    resolver = MediaLinkResolver()
    result = resolver.resolve([note], context)

    assert "[[Attachments/document.pdf]]" in result[0].body


def test_media_link_resolver_warns_on_unknown_checksum():
    context = make_context()

    note = Note(
        title="Note",
        source="evernote",
        body="Missing [UNOBIT-MEDIA:1:image/png:unknown]",
    )

    resolver = MediaLinkResolver()
    result = resolver.resolve([note], context)

    assert "[UNOBIT-MEDIA:1:image/png:unknown]" in result[0].body
    assert context.report.media_total == 1
    assert context.report.media_resolved == 0
    assert context.report.media_unresolved == 1
    assert len(context.report.warnings) == 1
    assert context.report.warnings[0].context["code"] == "evernote-media-unresolved"