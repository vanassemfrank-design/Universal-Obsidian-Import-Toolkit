from unobit.models import Note
from unobit.processors.content_cleanup_processor import ContentCleanupProcessor


def test_content_cleanup_processor_strips_body_whitespace():
    processor = ContentCleanupProcessor()

    note = Note(
        title="Test",
        source="test",
        body="\n\nMijn tekst\n\n",
    )

    result = processor.process(note)

    assert result.body == "Mijn tekst"


def test_content_cleanup_processor_ignores_missing_body():
    processor = ContentCleanupProcessor()

    item = object()

    result = processor.process(item)

    assert result is item