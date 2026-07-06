from pathlib import Path

from unobit.importers.base import BaseImporter
from unobit.models import Bookmark, KnowledgeItem, Note


class DummyImporter(BaseImporter):
    source_name = "dummy"

    def supports_file(self, path: Path) -> bool:
        return path.suffix.lower() == ".dummy"

    def import_file(self, path: Path) -> list[KnowledgeItem]:
        return [
            Note(
                title="Dummy Note",
                source=self.source_name,
                body=f"Imported from {path.name}",
                tags=["dummy", "test"],
            ),
            Bookmark(
                title="Dummy Bookmark",
                source=self.source_name,
                url="https://obsidian.md",
                folder="Demo",
                tags=["dummy", "bookmark"],
            ),
        ]