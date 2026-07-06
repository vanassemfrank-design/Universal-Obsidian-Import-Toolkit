from abc import ABC, abstractmethod
from pathlib import Path

from unobit.models import KnowledgeItem


class BaseExporter(ABC):
    name: str = "unknown"

    @abstractmethod
    def export_items(self, items: list[KnowledgeItem], output_path: Path) -> list[Path]:
        """Export knowledge items and return created file paths."""
        raise NotImplementedError