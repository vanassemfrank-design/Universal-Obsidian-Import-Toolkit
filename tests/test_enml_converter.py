from unobit.enml.converter import ENMLConverter


def test_enml_converter_converts_basic_note():
    converter = ENMLConverter()

    content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note><div>Hello ENML</div></en-note>
"""

    result = converter.convert(content)

    assert "Hello ENML" in result
    assert "<en-note>" not in result
    assert "</en-note>" not in result


def test_enml_converter_converts_todos():
    converter = ENMLConverter()

    content = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note>
<div><en-todo/> Open task</div>
<div><en-todo checked="true"/> Done task</div>
</en-note>
"""

    result = converter.convert(content)

    assert "- [ ] Open task" in result
    assert "- [x] Done task" in result