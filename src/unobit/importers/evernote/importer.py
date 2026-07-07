import base64
import hashlib
import mimetypes
from pathlib import Path
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from markdownify import markdownify as md

from unobit.importers.base import BaseImporter
from unobit.models import Attachment, KnowledgeItem, Note
from unobit.utils.dates import parse_evernote_datetime


class EvernoteImporter(BaseImporter):
    source_name = "evernote"

    def supports_file(self, path: Path) -> bool:
        return path.suffix.lower() == ".enex"

    def import_file(self, path: Path) -> list[KnowledgeItem]:
        tree = ET.parse(path)
        root = tree.getroot()

        notes: list[KnowledgeItem] = []

        for note_element in root.findall("note"):
            title = self._text(note_element, "title") or "Untitled"
            content = self._text(note_element, "content") or ""

            created_raw = self._text(note_element, "created")
            updated_raw = self._text(note_element, "updated")

            created = parse_evernote_datetime(created_raw)
            updated = parse_evernote_datetime(updated_raw)

            tags = [tag.text for tag in note_element.findall("tag") if tag.text]

            body = self._convert_enml_to_markdown(content)
            attachments = self._extract_attachments(note_element)

            note = Note(
                title=title,
                source=self.source_name,
                body=body,
                tags=tags,
                created_at=created,
                updated_at=updated,
                attachments=attachments,
                metadata={
                    "created_raw": created_raw,
                    "updated_raw": updated_raw,
                    "source_file": str(path),
                    "source_filename": path.name,
                    "attachment_count": len(attachments),
                },
            )

            notes.append(note)

        return notes

    def _text(self, element: ET.Element, tag: str) -> str | None:
        found = element.find(tag)
        if found is None:
            return None
        return found.text

    def _convert_enml_to_markdown(self, content: str) -> str:
        soup = BeautifulSoup(content, "lxml")

        en_note = soup.find("en-note")
        if en_note:
            html = str(en_note)
        else:
            html = content

        return md(html)

    def _extract_attachments(self, note_element: ET.Element) -> list[Attachment]:
        attachments: list[Attachment] = []

        for index, resource in enumerate(note_element.findall("resource"), start=1):
            mime_type = self._text(resource, "mime")
            data = resource.find("data")

            filename = None
            source_url = None

            attributes = resource.find("resource-attributes")
            if attributes is not None:
                filename = self._text(attributes, "file-name")
                source_url = self._text(attributes, "source-url")

            raw_bytes = b""
            checksum = None
            size_bytes = None

            if data is not None and data.text:
                clean_data = "".join(data.text.split())
                raw_bytes = base64.b64decode(clean_data)
                checksum = hashlib.md5(raw_bytes).hexdigest()
                size_bytes = len(raw_bytes)

            if not filename:
                extension = mimetypes.guess_extension(mime_type or "") or ".bin"

                if mime_type and mime_type.startswith("image/"):
                    prefix = "evernote-image"
                elif mime_type == "application/pdf":
                    prefix = "evernote-pdf"
                else:
                    prefix = "evernote-attachment"

                short_hash = checksum[:8] if checksum else f"{index:04d}"
                filename = f"{prefix}-{short_hash}{extension}"

            attachments.append(
                Attachment(
                    filename=filename,
                    mime_type=mime_type,
                    checksum=checksum,
                    size_bytes=size_bytes,
                    source_url=source_url,
                    data=raw_bytes if raw_bytes else None,
                )
            )

        return attachments