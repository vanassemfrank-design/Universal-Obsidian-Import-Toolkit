from pathlib import Path

from slugify import slugify

from unobit.exporters.base import BaseExporter
from unobit.models import Bookmark, KnowledgeItem, Note


class MarkdownExporter(BaseExporter):
    name = "markdown"

    def export_items(self, items: list[KnowledgeItem], output_path: Path) -> list[Path]:
        output_path.mkdir(parents=True, exist_ok=True)

        created_files: list[Path] = []

        for item in items:
            filename = self._safe_filename(item)
            file_path = output_path / filename
            file_path.write_text(self._to_markdown(item), encoding="utf-8")
            created_files.append(file_path)

        return created_files

    def _safe_filename(self, item: KnowledgeItem) -> str:
        base = slugify(item.title) or item.id
        return f"{base}.md"

    def _to_markdown(self, item: KnowledgeItem) -> str:
        frontmatter = self._frontmatter(item)

        if isinstance(item, Note):
            return f"{frontmatter}\n\n{item.body}\n"

        if isinstance(item, Bookmark):
            description = item.description or ""
            return f"{frontmatter}\n\n[{item.title}]({item.url})\n\n{description}\n"

        return f"{frontmatter}\n\n"
    
    def _frontmatter(self, item: KnowledgeItem) -> str:
        tags = "\n".join(f"  - {tag}" for tag in item.tags)

        return (
            "---\n"
            f"title: \"{item.title}\"\n"
            f"type: \"{item.item_type()}\"\n"
            f"source: \"{item.source}\"\n"
            f"id: \"{item.id}\"\n"
            "tags:\n"
            f"{tags if tags else '  []'}\n"
            "---"
        )