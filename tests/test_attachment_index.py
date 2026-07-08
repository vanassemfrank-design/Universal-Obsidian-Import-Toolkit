from unobit.models import Attachment, Note
from unobit.resolvers.attachment_index import AttachmentIndex


def test_attachment_index_finds_attachment_by_checksum():
    attachment = Attachment(
        filename="image.png",
        mime_type="image/png",
        checksum="ABC123",
    )

    note = Note(
        title="Note",
        source="test",
        body="",
        attachments=[attachment],
    )

    index = AttachmentIndex([note])

    assert index.get_by_checksum("abc123") == attachment


def test_attachment_index_returns_none_for_unknown_checksum():
    note = Note(
        title="Note",
        source="test",
        body="",
        attachments=[],
    )

    index = AttachmentIndex([note])

    assert index.get_by_checksum("missing") is None