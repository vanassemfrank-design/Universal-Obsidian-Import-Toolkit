from unobit.models import Note
from unobit.validators.note_validator import NoteValidator


def test_note_validator_warns_on_missing_title():
    validator = NoteValidator()

    note = Note(
        title="",
        source="test",
        body="Hello",
    )

    result = validator.validate(note)

    assert result.has_warnings is True
    assert result.messages[0].code == "note-missing-title"


def test_note_validator_errors_on_missing_body():
    validator = NoteValidator()

    note = Note(
        title="Title",
        source="test",
        body=None,
    )

    result = validator.validate(note)

    assert result.has_errors is True
    assert result.messages[0].code == "note-missing-body"


def test_note_validator_accepts_valid_note():
    validator = NoteValidator()

    note = Note(
        title="Title",
        source="test",
        body="Hello",
    )

    result = validator.validate(note)

    assert result.has_errors is False
    assert result.has_warnings is False