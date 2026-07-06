from unobit.utils.dates import parse_evernote_datetime
from pathlib import Path
import xml.etree.ElementTree as ET

from bs4 import BeautifulSoup
from markdownify import markdownify as md

from unobit.importers.base import BaseImporter
from unobit.models import KnowledgeItem, Note


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

            note = Note(
                title=title,
                source=self.source_name,
                body=body,
                tags=tags,
                created_at=created,
                updated_at=updated,
                metadata={
                    "created_raw": created_raw,
                    "updated_raw": updated_raw,
                    "source_file": str(path),
                    "source_filename": path.name,
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