from pathlib import Path

from slugify import slugify

from unobit.exporters.base import BaseExporter
from unobit.localization.labels import get_label
from unobit.models import Bookmark, KnowledgeItem, Note
from unobit.utils.dates import format_datetime


class MarkdownExporter(BaseExporter):
    name = "markdown"

    def __init__(self, language: str = "en"):
        self.language = language

    def export_items(self, items: list[KnowledgeItem], output_path: Path) -> list[Path]:
        output_path.mkdir(parents=True, exist_ok=True)

        created_files: list[Path] = []

        for item in items:
            if isinstance(item, Note):
                self._write_attachments(item, output_path)

            filename = self._safe_filename(item)
            file_path = output_path / filename
            file_path.write_text(self._to_markdown(item), encoding="utf-8")
            created_files.append(file_path)

        return created_files

    def _write_attachments(self, item: Note, output_path: Path) -> None:
        attachments_path = output_path / "Attachments"
        attachments_path.mkdir(parents=True, exist_ok=True)

        for attachment in item.attachments:
            if not attachment.data:
                continue

            target_path = attachments_path / attachment.filename
            target_path.write_bytes(attachment.data)
            attachment.path = target_path

    def _safe_filename(self, item: KnowledgeItem) -> str:
        base = slugify(item.title) or item.id
        return f"{base}.md"

    def _to_markdown(self, item: KnowledgeItem) -> str:
        frontmatter = self._frontmatter(item)

        if isinstance(item, Note):
            attachment_block = self._attachment_block(item)
            return f"{frontmatter}\n\n{item.body}\n{attachment_block}\n"

        if isinstance(item, Bookmark):
            description = item.description or ""
            return f"{frontmatter}\n\n[{item.title}]({item.url})\n\n{description}\n"

        return f"{frontmatter}\n\n"

    def _attachment_block(self, item: Note) -> str:
        if not item.attachments:
            return ""

        lines = [
            "",
            f"## {get_label('attachments', self.language)}",
            "",
        ]

        for attachment in item.attachments:
            obsidian_path = f"Attachments/{attachment.filename}"

            if attachment.mime_type and attachment.mime_type.startswith(
                ("image/", "audio/", "video/")
            ):
                lines.append(f"![[{obsidian_path}]]")
            elif attachment.mime_type == "application/pdf":
                lines.append(f"![[{obsidian_path}]]")
            else:
                lines.append(f"[[{obsidian_path}]]")

            if attachment.checksum:
                lines.append(f"<!-- checksum: {attachment.checksum} -->")

        return "\n".join(lines)

    def _frontmatter(self, item: KnowledgeItem) -> str:
        tags = "\n".join(f"  - {tag}" for tag in item.tags)

        lines = [
            "---",
            f'title: "{item.title}"',
            f'type: "{item.item_type()}"',
            f'source: "{item.source}"',
            f'id: "{item.id}"',
        ]

        created = format_datetime(item.created_at)
        updated = format_datetime(item.updated_at)

        if created:
            lines.append(f'created: "{created}"')

        if updated:
            lines.append(f'updated: "{updated}"')

        if item.metadata:
            lines.append("metadata:")
            for key, value in item.metadata.items():
                safe_value = str(value).replace('"', '\\"')
                lines.append(f'  {key}: "{safe_value}"')

        lines.append("tags:")
        lines.append(tags if tags else "  []")
        lines.append("---")

        return "\n".join(lines)