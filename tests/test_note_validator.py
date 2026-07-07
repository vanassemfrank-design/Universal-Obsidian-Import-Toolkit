from dataclasses import dataclass

from unobit.validators.note_validator import NoteValidator


@dataclass
class FakeNote:
    title: str | None
    content: str | None


def test_note_validator_warns_on_missing_title():
    validator = NoteValidator()

    result = validator.validate(FakeNote(title="", content="Hello"))

    assert result.has_warnings is True
    assert result.messages[0].code == "note-missing-title"


def test_note_validator_errors_on_missing_content():
    validator = NoteValidator()

    result = validator.validate(FakeNote(title="Title", content=None))

    assert result.has_errors is True
    assert result.messages[0].code == "note-missing-content"


def test_note_validator_accepts_valid_note():
    validator = NoteValidator()

    result = validator.validate(FakeNote(title="Title", content="Hello"))

    assert result.has_errors is False
    assert result.has_warnings is False
    assert result.messages == []