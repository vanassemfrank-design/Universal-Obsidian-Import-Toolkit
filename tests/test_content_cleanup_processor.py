from unobit.processors.content_cleanup_processor import ContentCleanupProcessor


class FakeNote:
    def __init__(self, content: str) -> None:
        self.content = content


def test_content_cleanup_processor_strips_content_whitespace():
    processor = ContentCleanupProcessor()

    note = FakeNote("\n\nMijn tekst\n\n")

    result = processor.process(note)

    assert result.content == "Mijn tekst"


def test_content_cleanup_processor_ignores_missing_content():
    processor = ContentCleanupProcessor()

    item = object()

    result = processor.process(item)

    assert result is item