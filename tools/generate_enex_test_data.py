from pathlib import Path
from xml.sax.saxutils import escape
import base64
import hashlib


OUTPUT_DIR = Path("tests/data/evernote")


def enml(body: str) -> str:
    return f"""<![CDATA[<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">
<en-note>{body}</en-note>]]>"""

def resource(
    data: bytes,
    mime_type: str,
    filename: str,
) -> tuple[str, str]:
    checksum = hashlib.md5(data).hexdigest()
    encoded = base64.b64encode(data).decode("ascii")

    xml = f"""  <resource>
    <data encoding="base64">{encoded}</data>
    <mime>{mime_type}</mime>
    <resource-attributes>
      <file-name>{escape(filename)}</file-name>
    </resource-attributes>
  </resource>
"""

    return xml, checksum

def note_with_resources(
    guid: str,
    title: str,
    body: str,
    resources: list[str],
    created: str = "20260708T090000Z",
    updated: str = "20260708T090000Z",
    tags: list[str] | None = None,
) -> str:
    tags_xml = ""

    for tag in tags or []:
        tags_xml += f"  <tag>{escape(tag)}</tag>\n"

    resources_xml = "\n".join(resources)

    return f"""<note>
  <guid>{escape(guid)}</guid>
  <title>{escape(title)}</title>
  <content>{enml(body)}</content>
  <created>{created}</created>
  <updated>{updated}</updated>
{tags_xml}{resources_xml}</note>
"""

def generate_enml_media_with_attachment() -> None:
    image_data = b"fake image content"
    pdf_data = b"%PDF-1.4 fake pdf content"

    image_resource, image_checksum = resource(
        data=image_data,
        mime_type="image/png",
        filename="test-image.png",
    )

    pdf_resource, pdf_checksum = resource(
        data=pdf_data,
        mime_type="application/pdf",
        filename="test-document.pdf",
    )

    body = f"""
<div>Image below:</div>
<div><en-media type="image/png" hash="{image_checksum}"/></div>
<div>PDF below:</div>
<div><en-media type="application/pdf" hash="{pdf_checksum}"/></div>
"""

    content = enex(
        [
            note_with_resources(
                guid="77777777-7777-7777-7777-777777777777",
                title="ENML Media With Attachment",
                body=body,
                resources=[image_resource, pdf_resource],
                tags=["test", "enml", "media", "attachments"],
            )
        ]
    )

    write_file("enml-media-with-attachment.enex", content)

def note(
    guid: str,
    title: str,
    body: str,
    created: str = "20260708T090000Z",
    updated: str = "20260708T090000Z",
    tags: list[str] | None = None,
) -> str:
    tags_xml = ""

    for tag in tags or []:
        tags_xml += f"  <tag>{escape(tag)}</tag>\n"

    return f"""<note>
  <guid>{escape(guid)}</guid>
  <title>{escape(title)}</title>
  <content>{enml(body)}</content>
  <created>{created}</created>
  <updated>{updated}</updated>
{tags_xml}</note>
"""


def enex(notes: list[str]) -> str:
    joined_notes = "\n".join(notes)

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export4.dtd">
<en-export export-date="20260708T090000Z" application="UNOBIT Test Generator" version="1.0">
{joined_notes}
</en-export>
"""


def write_file(filename: str, content: str) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUTPUT_DIR / filename
    path.write_text(content, encoding="utf-8")
    print(f"written: {path}")


def generate_internal_links() -> None:
    shopping_guid = "11111111-1111-1111-1111-111111111111"
    recipe_guid = "22222222-2222-2222-2222-222222222222"

    shopping_body = f"""
<div>See <a href="evernote:///view/12345/s1/{recipe_guid}/{recipe_guid}/">Recipe</a></div>
<div>Milk</div>
<div>Eggs</div>
<div>Bread</div>
"""

    recipe_body = f"""
<div>See <a href="evernote:///view/12345/s1/{shopping_guid}/{shopping_guid}/">Shopping List</a></div>
<div>Ingredients...</div>
"""

    content = enex(
        [
            note(
                guid=shopping_guid,
                title="Shopping List",
                body=shopping_body,
                tags=["test", "internal-links"],
            ),
            note(
                guid=recipe_guid,
                title="Recipe",
                body=recipe_body,
                tags=["test", "internal-links"],
            ),
        ]
    )

    write_file("internal-links.enex", content)


def generate_large_title() -> None:
    long_title = (
        "XM 1080 P draadloze PTZ IP camera wifi CMOS nachtzicht H264 "
        "PTZ IR security camera motion detection home security "
        "van bewakingscamera's op"
    )

    content = enex(
        [
            note(
                guid="33333333-3333-3333-3333-333333333333",
                title=long_title,
                body="<div>Large title filename regression test.</div>",
                tags=["test", "large-title"],
            )
        ]
    )

    write_file("large-title.enex", content)


def generate_invalid_internal_link() -> None:
    unknown_guid = "99999999-9999-9999-9999-999999999999"

    body = f"""
<div>See <a href="evernote:///view/12345/s1/{unknown_guid}/{unknown_guid}/">Missing Note</a></div>
<div>This link should remain unresolved.</div>
"""

    content = enex(
        [
            note(
                guid="44444444-4444-4444-4444-444444444444",
                title="Broken Link Source",
                body=body,
                tags=["test", "broken-links"],
            )
        ]
    )

    write_file("invalid-links.enex", content)


def main() -> None:
    generate_internal_links()
    generate_large_title()
    generate_invalid_internal_link()
    generate_enml_formatting()
    generate_media_placeholder()
    generate_enml_media_with_attachment()

def generate_enml_formatting() -> None:
    body = """
<div>First paragraph</div>
<div>Second paragraph with <b>bold</b> and <i>italic</i>.</div>
<br/>
<div><en-todo/> Open task</div>
<div><en-todo checked="true"/> Done task</div>
<hr/>
<ul>
  <li>Bullet one</li>
  <li>Bullet two</li>
</ul>
<ol>
  <li>Number one</li>
  <li>Number two</li>
</ol>
<table>
  <tr>
    <th>Name</th>
    <th>Status</th>
  </tr>
  <tr>
    <td>Import</td>
    <td>Done</td>
  </tr>
  <tr>
    <td>Export</td>
    <td>Planned</td>
  </tr>
</table>
"""

    content = enex(
        [
            note(
                guid="55555555-5555-5555-5555-555555555555",
                title="ENML Formatting",
                body=body,
                tags=["test", "enml", "formatting"],
            )
        ]
    )

    write_file("enml-formatting.enex", content)

def generate_media_placeholder() -> None:
    body = """
<div>Image below:</div>
<div><en-media type="image/png" hash="abc123"/></div>
<div>PDF below:</div>
<div><en-media type="application/pdf" hash="def456"/></div>
"""

    content = enex(
        [
            note(
                guid="66666666-6666-6666-6666-666666666666",
                title="ENML Media Placeholder",
                body=body,
                tags=["test", "enml", "media"],
            )
        ]
    )

    write_file("enml-media.enex", content)

if __name__ == "__main__":
    main()

