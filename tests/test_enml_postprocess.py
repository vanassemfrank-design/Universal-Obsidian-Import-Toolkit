from unobit.enml.postprocess import clean_markdown


def test_clean_markdown_removes_en_note_wrapper():
    markdown = "<en-note>\nHello\n</en-note>"

    result = clean_markdown(markdown)

    assert result == "Hello"


def test_clean_markdown_strips_trailing_whitespace():
    markdown = "Hello   \nWorld   \n"

    result = clean_markdown(markdown)

    assert result == "Hello\nWorld"