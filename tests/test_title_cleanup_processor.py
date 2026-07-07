from unobit.processors.title_cleanup_processor import TitleCleanupProcessor


class FakeNote:
    def __init__(self, title: str) -> None:
        self.title = title


def test_title_cleanup_processor_strips_title_whitespace():
    processor = TitleCleanupProcessor()

    note = FakeNote("  Mijn notitie  ")

    result = processor.process(note)

    assert result.title == "Mijn notitie"


def test_title_cleanup_processor_ignores_missing_title():
    processor = TitleCleanupProcessor()

    item = object()

    result = processor.process(item)

    assert result is item