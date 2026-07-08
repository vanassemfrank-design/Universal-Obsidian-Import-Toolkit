from unobit.enml.cleanup import (
    extract_en_note_html,
    normalize_whitespace,
    parse_enml,
    remove_empty_nodes,
)


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

def test_remove_empty_nodes():
    soup = parse_enml(
        """
<en-note>
<div></div>
<div>Hello</div>
<div>   </div>
</en-note>
"""
    )

    remove_empty_nodes(soup)

    assert str(soup).count("<div") == 1


def test_normalize_whitespace():
    soup = parse_enml(
        """
<en-note>
<div>Hello     world</div>
</en-note>
"""
    )

    normalize_whitespace(soup)

    assert "Hello world" in str(soup)