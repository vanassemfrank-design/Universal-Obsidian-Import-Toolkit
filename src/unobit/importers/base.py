from abc import ABC, abstractmethod
from pathlib import Path

from unobit.models import KnowledgeItem


class BaseImporter(ABC):
    source_name: str = "unknown"

    @abstractmethod
    def import_file(self, path: Path) -> list[KnowledgeItem]:
        """Import a single file and return universal knowledge items."""
        raise NotImplementedError

    def supports_file(self, path: Path) -> bool:
        """Return True if this importer supports the given file."""
        return False