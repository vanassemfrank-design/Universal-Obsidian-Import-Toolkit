from unobit.enml.cleanup import extract_en_note_html, parse_enml


def test_parse_enml_finds_en_note():
    content = """<?xml version="1.0" encoding="UTF-8"?>
<en-note><div>Hello</div></en-note>
"""

    soup = parse_enml(content)

    assert soup.find("en-note") is not None


def test_extract_en_note_html_returns_note_when_present():
    content = """<?xml version="1.0" encoding="UTF-8"?>
<en-note><div>Hello</div></en-note>
"""

    soup = parse_enml(content)

    html = extract_en_note_html(soup, fallback="fallback")

    assert "<en-note>" in html
    assert "Hello" in html


def test_extract_en_note_html_returns_fallback_when_missing():
    content = "<div>Hello</div>"

    soup = parse_enml(content)

    html = extract_en_note_html(soup, fallback=content)

    assert html == content