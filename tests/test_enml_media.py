from unobit.enml.cleanup import parse_enml
from unobit.enml.media import convert_media_placeholders


def test_convert_media_placeholders_replaces_en_media():
    soup = parse_enml(
        '<en-note><div><en-media type="image/png" hash="abc123"/></div></en-note>'
    )

    convert_media_placeholders(soup)

    result = str(soup)

    assert "UNOBIT-MEDIA" in result
    assert "image/png" in result
    assert "abc123" in result
    assert "en-media" not in result