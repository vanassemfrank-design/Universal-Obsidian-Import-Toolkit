# UNOBIT Source Bundle

Generated: 2026-07-11T08:57:28
Source: `C:\dev\vibecoded-pkm\Universal-Obsidian-Import-Toolkit\src\unobit`

---

## Files

- `src\unobit\__init__.py`
- `src\unobit\config\__init__.py`
- `src\unobit\config\settings.py`
- `src\unobit\config.py`
- `src\unobit\core\__init__.py`
- `src\unobit\core\batch_processing_step.py`
- `src\unobit\core\context.py`
- `src\unobit\core\performance.py`
- `src\unobit\core\pipeline.py`
- `src\unobit\core\pipeline_factory.py`
- `src\unobit\core\processing_step.py`
- `src\unobit\core\report.py`
- `src\unobit\core\resolution_step.py`
- `src\unobit\core\timed_step.py`
- `src\unobit\core\timing_step.py`
- `src\unobit\core\validation_step.py`
- `src\unobit\enml\__init__.py`
- `src\unobit\enml\attachment_index.py`
- `src\unobit\enml\cleanup.py`
- `src\unobit\enml\converter.py`
- `src\unobit\enml\media.py`
- `src\unobit\enml\postprocess.py`
- `src\unobit\enml\todos.py`
- `src\unobit\exporters\__init__.py`
- `src\unobit\exporters\base.py`
- `src\unobit\exporters\markdown.py`
- `src\unobit\exporters\obsidian.py`
- `src\unobit\gui\__init__.py`
- `src\unobit\gui\server.py`
- `src\unobit\importers\__init__.py`
- `src\unobit\importers\base.py`
- `src\unobit\importers\dummy\__init__.py`
- `src\unobit\importers\dummy\importer.py`
- `src\unobit\importers\evernote\__init__.py`
- `src\unobit\importers\evernote\importer.py`
- `src\unobit\localization\__init__.py`
- `src\unobit\localization\labels.py`
- `src\unobit\logger.py`
- `src\unobit\main.py`
- `src\unobit\models\__init__.py`
- `src\unobit\models\attachment.py`
- `src\unobit\models\bookmark.py`
- `src\unobit\models\knowledge_item.py`
- `src\unobit\models\link.py`
- `src\unobit\models\metadata.py`
- `src\unobit\models\note.py`
- `src\unobit\models\tag.py`
- `src\unobit\models\task.py`
- `src\unobit\pipeline\base.py`
- `src\unobit\processors\attachments.py`
- `src\unobit\processors\base.py`
- `src\unobit\processors\content_cleanup_processor.py`
- `src\unobit\processors\evernote_internal_link_processor.py`
- `src\unobit\processors\markdown.py`
- `src\unobit\processors\title_cleanup_processor.py`
- `src\unobit\processors\wikilinks.py`
- `src\unobit\processors\yaml.py`
- `src\unobit\reporters\__init__.py`
- `src\unobit\reporters\html_report.py`
- `src\unobit\reporters\json_report.py`
- `src\unobit\resolvers\__init__.py.py`
- `src\unobit\resolvers\attachment_index.py`
- `src\unobit\resolvers\base.py`
- `src\unobit\resolvers\evernote_links.py`
- `src\unobit\resolvers\media_links.py`
- `src\unobit\services\__init__.py`
- `src\unobit\services\import_service.py`
- `src\unobit\utils\__init__.py`
- `src\unobit\utils\dates.py`
- `src\unobit\validators\attachment_validator.py`
- `src\unobit\validators\base.py`
- `src\unobit\validators\link_validator.py`
- `src\unobit\validators\metadata_validator.py`
- `src\unobit\validators\note_validator.py`

---

## `src\unobit\__init__.py`

```python
"""
Universal Obsidian Import Toolkit (UNOBIT)

Import once. Preserve forever.
"""

__version__ = "0.1.0"
```

---

## `src\unobit\config\__init__.py`

```python

```

---

## `src\unobit\config\settings.py`

```python
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


SUPPORTED_LANGUAGES = {"en", "nl"}


class ConfigError(ValueError):
    """Raised when an UNOBIT configuration file is invalid."""


@dataclass
class UnobitSettings:
    output: str = "output/evernote"
    language: str = "en"
    json_report: bool = True
    html_report: bool = False


def load_settings(
    path: str | Path = "unobit.yaml",
) -> UnobitSettings:
    config_path = Path(path)

    if not config_path.exists():
        return UnobitSettings()

    try:
        raw_data = config_path.read_text(encoding="utf-8")
        loaded_data = yaml.safe_load(raw_data)
    except OSError as error:
        raise ConfigError(
            f"Could not read configuration file: {config_path}"
        ) from error
    except yaml.YAMLError as error:
        raise ConfigError(
            f"Invalid YAML in configuration file: {config_path}"
        ) from error

    if loaded_data is None:
        data: dict[str, Any] = {}
    elif isinstance(loaded_data, dict):
        data = loaded_data
    else:
        raise ConfigError(
            "Configuration root must be a YAML object."
        )

    settings = UnobitSettings(
        output=_read_string(
            data,
            key="output",
            default="output/evernote",
        ),
        language=_read_string(
            data,
            key="language",
            default="en",
        ).lower(),
        json_report=_read_boolean(
            data,
            key="json_report",
            default=True,
        ),
        html_report=_read_boolean(
            data,
            key="html_report",
            default=False,
        ),
    )

    validate_settings(settings)

    return settings


def validate_settings(settings: UnobitSettings) -> None:
    if not settings.output.strip():
        raise ConfigError(
            "Configuration value 'output' cannot be empty."
        )

    if settings.language not in SUPPORTED_LANGUAGES:
        supported = ", ".join(sorted(SUPPORTED_LANGUAGES))

        raise ConfigError(
            "Unsupported language "
            f"'{settings.language}'. Supported: {supported}."
        )

    if not settings.json_report and not settings.html_report:
        raise ConfigError(
            "At least one report format must be enabled: "
            "'json_report' or 'html_report'."
        )


def write_default_settings(
    path: str | Path = "unobit.yaml",
) -> Path:
    config_path = Path(path)

    if config_path.exists():
        return config_path

    config_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    config_path.write_text(
        "\n".join(
            [
                "output: output/evernote",
                "language: en",
                "json_report: true",
                "html_report: false",
                "",
            ]
        ),
        encoding="utf-8",
    )

    return config_path


def _read_string(
    data: dict[str, Any],
    key: str,
    default: str,
) -> str:
    value = data.get(key, default)

    if not isinstance(value, str):
        raise ConfigError(
            f"Configuration value '{key}' must be a string."
        )

    return value


def _read_boolean(
    data: dict[str, Any],
    key: str,
    default: bool,
) -> bool:
    value = data.get(key, default)

    if not isinstance(value, bool):
        raise ConfigError(
            f"Configuration value '{key}' must be true or false."
        )

    return value
```

---

## `src\unobit\config.py`

```python
from pathlib import Path
import yaml


class Config:

    def __init__(self, filename: str = "config/config.yaml"):

        self.filename = Path(filename)

        if not self.filename.exists():
            self.filename = Path("config/config.example.yaml")

        with open(self.filename, encoding="utf-8") as f:
            self.data = yaml.safe_load(f)

    def get(self, *keys):

        value = self.data

        for key in keys:
            value = value[key]

        return value
```

---

## `src\unobit\core\__init__.py`

```python

```

---

## `src\unobit\core\batch_processing_step.py`

```python
from collections.abc import Iterable

from unobit.core.context import PipelineContext


class BatchProcessingStep:
    def __init__(self, processors: list[object]) -> None:
        self.processors = processors

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        current = list(items)

        for processor in self.processors:
            current = processor.process_all(current, context)

        return current
```

---

## `src\unobit\core\context.py`

```python
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from unobit.core.report import ImportReport


@dataclass
class PipelineContext:
    source_path: Path
    output_path: Path
    importer_name: str
    report: ImportReport
    options: dict[str, Any] = field(default_factory=dict)
```

---

## `src\unobit\core\performance.py`

```python
import tracemalloc


class MemoryMonitor:

    def start(self):
        tracemalloc.start()

    def stop(self):
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        return peak / 1024 / 1024
```

---

## `src\unobit\core\pipeline.py`

```python
from collections.abc import Iterable
from typing import Protocol

from unobit.core.context import PipelineContext


class PipelineStep(Protocol):
    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        ...


class ProcessingPipeline:
    def __init__(self, steps: list[PipelineStep] | None = None) -> None:
        self.steps = steps or []

    def add_step(self, step: PipelineStep) -> None:
        self.steps.append(step)

    def run(self, items: Iterable[object], context: PipelineContext) -> list[object]:
        current: Iterable[object] = items

        for step in self.steps:
            current = step.run(current, context)

        return list(current)
    
    def with_step(self, step: PipelineStep) -> "ProcessingPipeline":
        self.add_step(step)
        return self
```

---

## `src\unobit\core\pipeline_factory.py`

```python
from unobit.core.pipeline import ProcessingPipeline
from unobit.core.processing_step import ProcessingStep
from unobit.core.timed_step import TimedStep
from unobit.core.validation_step import ValidationStep
from unobit.processors.content_cleanup_processor import ContentCleanupProcessor
from unobit.processors.title_cleanup_processor import TitleCleanupProcessor
from unobit.validators.attachment_validator import AttachmentValidator
from unobit.validators.metadata_validator import MetadataValidator
from unobit.validators.note_validator import NoteValidator
from unobit.core.batch_processing_step import BatchProcessingStep
from unobit.processors.evernote_internal_link_processor import EvernoteInternalLinkProcessor
from unobit.core.resolution_step import ResolutionStep
from unobit.resolvers.evernote_links import EvernoteInternalLinkResolver
from unobit.resolvers.media_links import MediaLinkResolver

class PipelineFactory:
    @staticmethod
    def create_default() -> ProcessingPipeline:
        return ProcessingPipeline(
            steps=[
                TimedStep(
                    "validation",
                    ValidationStep(
                        validators=[
                            NoteValidator(),
                            AttachmentValidator(),
                            MetadataValidator(),
                        ]
                    ),
                ),
                TimedStep(
                    "processing",
                    ProcessingStep(
                        processors=[
                            TitleCleanupProcessor(),
                            ContentCleanupProcessor(),
                        ]
                    ),
                ),
                TimedStep(
                    "resolution",
                    ResolutionStep(
                        resolvers=[
                            EvernoteInternalLinkResolver(),
                            MediaLinkResolver(),
                        ]
                    ),
                ),
                TimedStep(
                    "evernote-links",
                    BatchProcessingStep(
                        processors=[
                            EvernoteInternalLinkProcessor(),
                        ]
                    ),
                ),
            ]
        )
```

---

## `src\unobit\core\processing_step.py`

```python
from collections.abc import Iterable

from unobit.core.context import PipelineContext
from unobit.processors.base import Processor


class ProcessingStep:
    def __init__(self, processors: list[Processor]) -> None:
        self.processors = processors

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        for item in items:
            current = item

            for processor in self.processors:
                current = processor.process(current)

            yield current
```

---

## `src\unobit\core\report.py`

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class ImportMessage:
    level: str
    message: str
    context: dict[str, Any] = field(default_factory=dict)


@dataclass
class ImportReport:
    source: str
    importer: str
    started_at: datetime = field(default_factory=datetime.now)
    finished_at: datetime | None = None

    notes_total: int = 0
    notes_success: int = 0
    notes_failed: int = 0

    attachments_total: int = 0
    attachments_exported: int = 0
    attachments_failed: int = 0

    media_total: int = 0
    media_resolved: int = 0
    media_unresolved: int = 0

    notes_per_second: float = 0.0
    attachments_per_second: float = 0.0

    peak_memory_mb: float | None = None

    largest_note_bytes: int = 0
    largest_attachment_bytes: int = 0

    warnings: list[ImportMessage] = field(default_factory=list)
    errors: list[ImportMessage] = field(default_factory=list)

    metadata: dict[str, Any] = field(default_factory=dict)

    def finish(self) -> None:
        self.finished_at = datetime.now()

    def add_warning(self, message: str, **context: Any) -> None:
        self.warnings.append(
            ImportMessage(level="warning", message=message, context=context)
        )

    def add_error(self, message: str, **context: Any) -> None:
        self.errors.append(
            ImportMessage(level="error", message=message, context=context)
        )

    timings: dict[str, float] = field(default_factory=dict)

    def add_timing(self, name: str, seconds: float) -> None:
        self.timings[name] = self.timings.get(name, 0.0) + seconds

    def format_duration(self, seconds: float) -> str:
        """
        Format a duration using the most appropriate unit.
        """

        if seconds >= 60:
            minutes = int(seconds // 60)
            remaining = seconds % 60
            return f"{minutes} min {remaining:.2f} s"

        if seconds >= 1:
            return f"{seconds:.2f} s"

        if seconds >= 0.001:
            return f"{seconds * 1000:.2f} ms"

        return f"{seconds * 1_000_000:.0f} µs"
    
    def calculate_statistics(self) -> None:
        duration = self.duration_seconds

        if duration is None or duration <= 0:
            return

        self.notes_per_second = self.notes_success / duration
        self.attachments_per_second = self.attachments_exported / duration
    
    @property
    def duration_seconds(self) -> float | None:
        if self.finished_at is None:
            return None

        return (self.finished_at - self.started_at).total_seconds()
```

---

## `src\unobit\core\resolution_step.py`

```python
from unobit.core.context import PipelineContext
from unobit.resolvers.base import Resolver


class ResolutionStep:

    def __init__(self, resolvers: list[Resolver]):
        self.resolvers = resolvers

    def run(self, items, context: PipelineContext):

        current = list(items)

        for resolver in self.resolvers:
            current = resolver.resolve(current, context)

        return current
```

---

## `src\unobit\core\timed_step.py`

```python
from collections.abc import Iterable
from time import perf_counter

from unobit.core.context import PipelineContext


class TimedStep:
    def __init__(self, name: str, step: object) -> None:
        self.name = name
        self.step = step

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        start = perf_counter()

        result = list(self.step.run(items, context))

        elapsed = perf_counter() - start
        context.report.add_timing(self.name, elapsed)

        return result
```

---

## `src\unobit\core\timing_step.py`

```python
from collections.abc import Iterable
from time import perf_counter

from unobit.core.context import PipelineContext


class TimingStep:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        start = perf_counter()

        try:
            for item in items:
                yield item
        finally:
            elapsed = perf_counter() - start
            context.report.add_timing(self.name, elapsed)
```

---

## `src\unobit\core\validation_step.py`

```python
from collections.abc import Iterable

from unobit.core.context import PipelineContext
from unobit.validators.base import Validator


class ValidationStep:
    def __init__(self, validators: list[Validator]) -> None:
        self.validators = validators

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        for item in items:
            for validator in self.validators:
                result = validator.validate(item)

                for message in result.messages:
                    if message.level == "error":
                        context.report.add_error(
                            message.message,
                            code=message.code,
                            **(message.context or {}),
                        )
                    elif message.level == "warning":
                        context.report.add_warning(
                            message.message,
                            code=message.code,
                            **(message.context or {}),
                        )

            yield item
```

---

## `src\unobit\enml\__init__.py`

```python

```

---

## `src\unobit\enml\attachment_index.py`

```python
from unobit.models import Attachment, Note


class AttachmentIndex:
    def __init__(self, notes: list[Note]) -> None:
        self.by_hash: dict[str, Attachment] = {}

        for note in notes:
            for attachment in note.attachments:
                if attachment.checksum:
                    self.by_hash[attachment.checksum.lower()] = attachment

    def get(self, checksum: str):
        return self.by_hash.get(checksum.lower())
```

---

## `src\unobit\enml\cleanup.py`

```python
from bs4 import BeautifulSoup, Tag


def parse_enml(content: str) -> BeautifulSoup:
    return BeautifulSoup(content, features="xml")


def remove_empty_nodes(soup: BeautifulSoup) -> None:
    """
    Remove empty XML nodes except media/todo/br/hr.
    """

    keep = {
        "en-media",
        "en-todo",
        "br",
        "hr",
    }

    changed = True

    while changed:
        changed = False

        for tag in list(soup.find_all()):
            if not isinstance(tag, Tag):
                continue

            if tag.name in keep:
                continue

            if tag.text.strip():
                continue

            if tag.find():
                continue

            tag.decompose()
            changed = True


def normalize_whitespace(soup: BeautifulSoup) -> None:
    """
    Remove excessive whitespace from text nodes.
    """

    for text in soup.find_all(string=True):
        text.replace_with(" ".join(text.split()))


def extract_en_note_html(
    soup: BeautifulSoup,
    fallback: str,
) -> str:
    en_note = soup.find("en-note")

    if en_note:
        return str(en_note)

    return fallback
```

---

## `src\unobit\enml\converter.py`

```python
from markdownify import markdownify as md
from unobit.enml.media import convert_media_placeholders

from unobit.enml.cleanup import (
    extract_en_note_html,
    normalize_whitespace,
    parse_enml,
    remove_empty_nodes,
)
from unobit.enml.postprocess import clean_markdown
from unobit.enml.todos import convert_todos


class ENMLConverter:
    def convert(self, content: str) -> str:
        soup = parse_enml(content)
        
        remove_empty_nodes(soup)
        normalize_whitespace(soup)
        convert_todos(soup)
        convert_media_placeholders(soup)

        html = extract_en_note_html(soup, fallback=content)

        markdown = md(
            html,
            heading_style="ATX",
            bullets="-",
        )

        return clean_markdown(markdown)
```

---

## `src\unobit\enml\media.py`

```python
from bs4 import BeautifulSoup


def convert_media_placeholders(soup: BeautifulSoup) -> None:
    for index, media in enumerate(soup.find_all("en-media"), start=1):
        media_type = media.get("type") or "application/octet-stream"
        media_hash = media.get("hash") or ""

        placeholder = f"[UNOBIT-MEDIA:{index}:{media_type}:{media_hash}]"

        media.replace_with(placeholder)
```

---

## `src\unobit\enml\postprocess.py`

```python
import re


def clean_markdown(markdown: str) -> str:
    markdown = markdown.replace("<en-note>", "")
    markdown = markdown.replace("</en-note>", "")

    lines = [line.rstrip() for line in markdown.splitlines()]

    markdown = "\n".join(lines)

    markdown = re.sub(r"\n{3,}", "\n\n", markdown)

    markdown = re.sub(r"[ \t]+$", "", markdown, flags=re.MULTILINE)

    return markdown.strip()
```

---

## `src\unobit\enml\todos.py`

```python
from bs4 import BeautifulSoup


def convert_todos(soup: BeautifulSoup) -> None:
    for todo in soup.find_all("en-todo"):
        checked = todo.get("checked") == "true"
        replacement = "- [x] " if checked else "- [ ] "
        todo.replace_with(replacement)
```

---

## `src\unobit\exporters\__init__.py`

```python
from unobit.exporters.base import BaseExporter
from unobit.exporters.markdown import MarkdownExporter

__all__ = [
    "BaseExporter",
    "MarkdownExporter",
]
```

---

## `src\unobit\exporters\base.py`

```python
from abc import ABC, abstractmethod
from pathlib import Path

from unobit.models import KnowledgeItem


class BaseExporter(ABC):
    name: str = "unknown"

    @abstractmethod
    def export_items(self, items: list[KnowledgeItem], output_path: Path) -> list[Path]:
        """Export knowledge items and return created file paths."""
        raise NotImplementedError
```

---

## `src\unobit\exporters\markdown.py`

```python
import mimetypes
import re
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

        used_filenames: set[str] = set()

        for index, attachment in enumerate(item.attachments, start=1):
            if not attachment.data:
                continue

            safe_filename = self._safe_attachment_filename(
                filename=attachment.filename,
                mime_type=attachment.mime_type,
                checksum=attachment.checksum,
                index=index,
                used_filenames=used_filenames,
            )

            target_path = attachments_path / safe_filename
            target_path.write_bytes(attachment.data)

            attachment.filename = safe_filename
            attachment.path = target_path

    def _safe_attachment_filename(
        self,
        filename: str | None,
        mime_type: str | None,
        checksum: str | None,
        index: int,
        used_filenames: set[str],
    ) -> str:
        original = filename or ""

        cleaned = original.strip()
        cleaned = cleaned.replace("\\", "/")
        cleaned = cleaned.split("/")[-1]

        cleaned = re.sub(r'[<>:"/\\|?*&=]', "-", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()
        cleaned = cleaned.strip(". ")

        if not cleaned or cleaned.startswith("-format-"):
            extension = mimetypes.guess_extension(mime_type or "") or ".bin"
            short_hash = checksum[:8] if checksum else f"{index:04d}"
            cleaned = f"evernote-attachment-{short_hash}{extension}"

        if "." not in Path(cleaned).name:
            extension = mimetypes.guess_extension(mime_type or "") or ".bin"
            cleaned = f"{cleaned}{extension}"

        base = Path(cleaned).stem
        suffix = Path(cleaned).suffix

        candidate = cleaned
        counter = 2

        while candidate.lower() in used_filenames:
            candidate = f"{base}-{counter}{suffix}"
            counter += 1

        used_filenames.add(candidate.lower())

        return candidate

    def _safe_filename(self, item: KnowledgeItem) -> str:
        base = slugify(item.title) or item.id

        short_id = str(item.id)[:8]
        max_base_length = 100

        if len(base) > max_base_length:
            base = base[:max_base_length].rstrip("-")

        return f"{base}-{short_id}.md"

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
```

---

## `src\unobit\exporters\obsidian.py`

```python

```

---

## `src\unobit\gui\__init__.py`

```python

```

---

## `src\unobit\gui\server.py`

```python
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import os
import webbrowser


def start_gui(
    host: str = "127.0.0.1",
    port: int = 8765,
    open_browser: bool = True,
) -> None:
    gui_path = Path(__file__).parent
    os.chdir(gui_path)

    url = f"http://{host}:{port}"

    if open_browser:
        webbrowser.open(url)

    server = ThreadingHTTPServer(
        (host, port),
        SimpleHTTPRequestHandler,
    )

    print(f"UNOBIT GUI running at {url}")
    print("Press Ctrl+C to stop.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        print("UNOBIT GUI stopped.")
    finally:
        server.server_close()
```

---

## `src\unobit\importers\__init__.py`

```python
from unobit.importers.base import BaseImporter
from unobit.importers.dummy import DummyImporter
from unobit.importers.evernote import EvernoteImporter

__all__ = [
    "BaseImporter",
    "DummyImporter",
    "EvernoteImporter",
]
```

---

## `src\unobit\importers\base.py`

```python
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
```

---

## `src\unobit\importers\dummy\__init__.py`

```python
from unobit.importers.dummy.importer import DummyImporter

__all__ = ["DummyImporter"]
```

---

## `src\unobit\importers\dummy\importer.py`

```python
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
```

---

## `src\unobit\importers\evernote\__init__.py`

```python
from unobit.importers.evernote.importer import EvernoteImporter

__all__ = ["EvernoteImporter"]
```

---

## `src\unobit\importers\evernote\importer.py`

```python
import base64
import hashlib
import mimetypes
from pathlib import Path
import xml.etree.ElementTree as ET

from unobit.importers.base import BaseImporter
from unobit.models import Attachment, KnowledgeItem, Note
from unobit.utils.dates import parse_evernote_datetime
from unobit.enml.converter import ENMLConverter


class EvernoteImporter(BaseImporter):
    source_name = "evernote"

    def supports_file(self, path: Path) -> bool:
        return path.suffix.lower() == ".enex"

    def import_file(self, path: Path) -> list[KnowledgeItem]:
        tree = ET.parse(path)
        root = tree.getroot()

        notes: list[KnowledgeItem] = []
        converter = ENMLConverter()

        for note_element in root.findall("note"):
            guid = self._text(note_element, "guid")
            title = self._text(note_element, "title") or "Untitled"
            content = self._text(note_element, "content") or ""

            created_raw = self._text(note_element, "created")
            updated_raw = self._text(note_element, "updated")

            created = parse_evernote_datetime(created_raw)
            updated = parse_evernote_datetime(updated_raw)

            tags = [tag.text for tag in note_element.findall("tag") if tag.text]

            body = converter.convert(content)
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
                    "guid": guid,
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
```

---

## `src\unobit\localization\__init__.py`

```python

```

---

## `src\unobit\localization\labels.py`

```python
LABELS = {
    "en": {
        "attachments": "Attachments",
    },
    "nl": {
        "attachments": "Bijlagen",
    },
}


def get_label(key: str, language: str = "en") -> str:
    return LABELS.get(language, LABELS["en"]).get(key, key)
```

---

## `src\unobit\logger.py`

```python
import logging


def get_logger(name: str):

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
    )

    return logging.getLogger(name)
```

---

## `src\unobit\main.py`

```python
import json
from pathlib import Path

import typer
from rich import print

from unobit import __version__
from unobit.config.settings import (
    ConfigError,
    load_settings,
    write_default_settings,
)
from unobit.exporters import MarkdownExporter
from unobit.gui.server import start_gui
from unobit.importers import DummyImporter, EvernoteImporter
from unobit.models import Bookmark, Note
from unobit.services.import_service import run_evernote_import


app = typer.Typer(
    help="Universal Obsidian Import Toolkit",
)

import_app = typer.Typer(
    help="Import knowledge archives.",
)

config_app = typer.Typer(
    help="Manage UNOBIT configuration.",
)

report_app = typer.Typer(
    help="View UNOBIT import reports.",
)

gui_app = typer.Typer(
    help="Start the local UNOBIT GUI.",
)

app.add_typer(import_app, name="import")
app.add_typer(config_app, name="config")
app.add_typer(report_app, name="report")
app.add_typer(gui_app, name="gui")


@app.command()
def info() -> None:
    """Show information about UNOBIT."""

    print()
    print("[bold]Universal Obsidian Import Toolkit[/bold]")
    print("UNOBIT")
    print(f"Version {__version__}")
    print()


@app.command()
def version() -> None:
    """Show the installed UNOBIT version."""

    print(__version__)


@app.command()
def demo() -> None:
    """Show example universal knowledge objects."""

    note = Note(
        title="Example Evernote Note",
        source="evernote",
        notebook="Inbox",
        body="This is a universal note object.",
        tags=["example", "evernote"],
    )

    bookmark = Bookmark(
        title="Obsidian",
        source="chrome",
        url="https://obsidian.md",
        folder="PKM/Tools",
        tags=["pkm", "tool"],
    )

    print("[bold]UNOBIT Demo Objects[/bold]")
    print()
    print(note)
    print()
    print(bookmark)


@app.command()
def import_dummy(
    path: str = "samples/dummy/example.dummy",
) -> None:
    """Import a dummy test file."""

    importer = DummyImporter()
    import_path = Path(path)

    if not importer.supports_file(import_path):
        print(f"[red]Unsupported file:[/red] {import_path}")
        raise typer.Exit(code=1)

    items = importer.import_file(import_path)

    print(
        f"[bold]Imported {len(items)} items "
        f"from {import_path}[/bold]"
    )
    print()

    for item in items:
        print(item)
        print()


@app.command()
def export_demo(
    output: str = "output/demo",
) -> None:
    """Export example objects to Markdown."""

    note = Note(
        title="Example Evernote Note",
        source="evernote",
        notebook="Inbox",
        body=(
            "This is a universal note object "
            "exported to Markdown."
        ),
        tags=["example", "evernote"],
    )

    bookmark = Bookmark(
        title="Obsidian",
        source="chrome",
        url="https://obsidian.md",
        folder="PKM/Tools",
        tags=["pkm", "tool"],
    )

    exporter = MarkdownExporter()

    created_files = exporter.export_items(
        [note, bookmark],
        Path(output),
    )

    print(
        f"[bold]Exported {len(created_files)} "
        f"files to {output}[/bold]"
    )
    print()

    for file_path in created_files:
        print(file_path)


@import_app.command("evernote")
def import_evernote(
    path: str,
    output: str | None = typer.Option(
        None,
        "--output",
        "-o",
        help="Override the configured output directory.",
    ),
    config: str = typer.Option(
        "unobit.yaml",
        "--config",
        "-c",
        help="Path to the UNOBIT configuration file.",
    ),
) -> None:
    """Import an Evernote ENEX archive."""

    try:
        settings = load_settings(config)
    except ConfigError as error:
        print(f"[red]Configuration error:[/red] {error}")
        raise typer.Exit(code=2) from error
    resolved_output = output or settings.output
    output_path = Path(resolved_output)

    try:
        report = run_evernote_import(
            path=path,
            output=resolved_output,
            language=settings.language,
            json_report=settings.json_report,
            html_report=settings.html_report,
        )
    except ValueError as error:
        print(f"[red]{error}[/red]")
        raise typer.Exit(code=1) from error
    except Exception as error:
        print(f"[red]Import failed:[/red] {error}")
        raise typer.Exit(code=1) from error

    print()
    print("[bold]UNOBIT Import Summary[/bold]")
    print("------------------------------------")
    print(f"Importer     : {report.importer}")
    print(f"Source       : {report.source}")

    print()
    print("Notes")
    print(f"  Imported   : {report.notes_total}")
    print(f"  Exported   : {report.notes_success}")
    print(f"  Failed     : {report.notes_failed}")

    print()
    print("Attachments")
    print(f"  Total      : {report.attachments_total}")
    print(f"  Exported   : {report.attachments_exported}")
    print(f"  Failed     : {report.attachments_failed}")

    print()
    print("Media")
    print(f"  Total      : {report.media_total}")
    print(f"  Resolved   : {report.media_resolved}")
    print(f"  Unresolved : {report.media_unresolved}")

    print()
    print(f"Warnings     : {len(report.warnings)}")
    print(f"Errors       : {len(report.errors)}")

    if report.timings:
        print()
        print("Timings")

        for name, seconds in report.timings.items():
            print(
                f"  {name:<12}: "
                f"{report.format_duration(seconds)}"
            )

    if report.duration_seconds is not None:
        print()
        print(
            "Total time   : "
            f"{report.format_duration(report.duration_seconds)}"
        )

    print()
    print("Performance")
    print(
        f"  Notes/sec       : "
        f"{report.notes_per_second:.2f}"
    )
    print(
        f"  Attachments/sec : "
        f"{report.attachments_per_second:.2f}"
    )

    if report.peak_memory_mb is not None:
        print(
            f"  Peak memory     : "
            f"{report.peak_memory_mb:.2f} MB"
        )

    print()
    print(f"Output       : {output_path}")

    if settings.json_report:
        print(
            f"JSON report  : "
            f"{output_path / 'import-report.json'}"
        )

    if settings.html_report:
        print(
            f"HTML report  : "
            f"{output_path / 'import-report.html'}"
        )

    print("------------------------------------")


@config_app.command("init")
def config_init(
    path: str = typer.Argument(
        "unobit.yaml",
        help="Path for the configuration file.",
    ),
) -> None:
    """Create a default UNOBIT configuration file."""

    config_path = Path(path)
    existed = config_path.exists()

    result_path = write_default_settings(config_path)

    if existed:
        print(
            "[yellow]Configuration already exists:[/yellow] "
            f"{result_path}"
        )
    else:
        print(
            "[green]Configuration created:[/green] "
            f"{result_path}"
        )


@config_app.command("show")
def config_show(
    path: str = typer.Argument(
        "unobit.yaml",
        help="Path to the configuration file.",
    ),
) -> None:
    """Show the active UNOBIT configuration."""

    try:
        settings = load_settings(path)
    except ConfigError as error:
        print(f"[red]Configuration error:[/red] {error}")
        raise typer.Exit(code=2) from error

    print()
    print("[bold]UNOBIT Configuration[/bold]")
    print("------------------------------------")
    print(f"File        : {Path(path)}")
    print(f"Output      : {settings.output}")
    print(f"Language    : {settings.language}")
    print(f"JSON report : {settings.json_report}")
    print(f"HTML report : {settings.html_report}")
    print("------------------------------------")


@report_app.command("show")
def report_show(path: str) -> None:
    """Display a JSON import report in the terminal."""

    report_path = Path(path)

    if not report_path.exists():
        print(f"[red]Report not found:[/red] {report_path}")
        raise typer.Exit(code=1)

    try:
        data = json.loads(
            report_path.read_text(encoding="utf-8")
        )
    except json.JSONDecodeError as error:
        print(
            f"[red]Invalid JSON report:[/red] "
            f"{report_path}"
        )
        raise typer.Exit(code=1) from error

    print()
    print("[bold]UNOBIT Report[/bold]")
    print("------------------------------------")
    print(f"Importer     : {data.get('importer', 'unknown')}")
    print(f"Source       : {data.get('source', 'unknown')}")

    print()
    print("Notes")
    print(f"  Imported   : {data.get('notes_total', 0)}")
    print(f"  Exported   : {data.get('notes_success', 0)}")
    print(f"  Failed     : {data.get('notes_failed', 0)}")

    print()
    print("Attachments")
    print(
        f"  Total      : "
        f"{data.get('attachments_total', 0)}"
    )
    print(
        f"  Exported   : "
        f"{data.get('attachments_exported', 0)}"
    )
    print(
        f"  Failed     : "
        f"{data.get('attachments_failed', 0)}"
    )

    print()
    print("Media")
    print(f"  Total      : {data.get('media_total', 0)}")
    print(f"  Resolved   : {data.get('media_resolved', 0)}")
    print(
        f"  Unresolved : "
        f"{data.get('media_unresolved', 0)}"
    )

    print()
    print(
        f"Warnings     : "
        f"{len(data.get('warnings', []))}"
    )
    print(
        f"Errors       : "
        f"{len(data.get('errors', []))}"
    )
    print("------------------------------------")


@gui_app.command("start")
def gui_start(
    host: str = "127.0.0.1",
    port: int = 8765,
    no_browser: bool = False,
) -> None:
    """Start the local HTML/JavaScript GUI."""

    start_gui(
        host=host,
        port=port,
        open_browser=not no_browser,
    )


@app.command()
def debug_evernote(path: str) -> None:
    """Show basic debugging information for an ENEX file."""

    import_path = Path(path)
    importer = EvernoteImporter()

    if not import_path.exists():
        print(f"[red]Source file not found:[/red] {import_path}")
        raise typer.Exit(code=1)

    items = importer.import_file(import_path)

    print("[bold]Debug Evernote import[/bold]")
    print(f"File: {import_path}")
    print(f"Items: {len(items)}")
    print()

    for item in items:
        attachments = getattr(item, "attachments", [])
        attachment_count = len(attachments)

        print(f"- {item.title}")
        print(f"  attachments: {attachment_count}")

        for attachment in attachments:
            print(f"    - filename: {attachment.filename}")
            print(f"      mime: {attachment.mime_type}")
            print(f"      checksum: {attachment.checksum}")
            print(f"      size: {attachment.size_bytes}")
```

---

## `src\unobit\models\__init__.py`

```python
from unobit.models.attachment import Attachment
from unobit.models.bookmark import Bookmark
from unobit.models.knowledge_item import KnowledgeItem
from unobit.models.link import Link
from unobit.models.note import Note

__all__ = [
    "Attachment",
    "Bookmark",
    "KnowledgeItem",
    "Link",
    "Note",
]
```

---

## `src\unobit\models\attachment.py`

```python
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Attachment:
    filename: str
    path: Path | None = None
    mime_type: str | None = None
    checksum: str | None = None
    size_bytes: int | None = None
    source_ref: str | None = None
    source_url: str | None = None
    data: bytes | None = None
```

---

## `src\unobit\models\bookmark.py`

```python
from dataclasses import dataclass

from unobit.models.knowledge_item import KnowledgeItem


@dataclass
class Bookmark(KnowledgeItem):
    url: str = ""
    folder: str | None = None
    description: str | None = None
```

---

## `src\unobit\models\knowledge_item.py`

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass
class KnowledgeItem:
    title: str
    source: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime | None = None
    updated_at: datetime | None = None
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def item_type(self) -> str:
        return self.__class__.__name__.lower()
```

---

## `src\unobit\models\link.py`

```python
from dataclasses import dataclass


@dataclass
class Link:
    target: str
    label: str | None = None
    is_internal: bool = False
    is_broken: bool = False
```

---

## `src\unobit\models\metadata.py`

```python

```

---

## `src\unobit\models\note.py`

```python
from dataclasses import dataclass, field

from unobit.models.attachment import Attachment
from unobit.models.knowledge_item import KnowledgeItem
from unobit.models.link import Link


@dataclass
class Note(KnowledgeItem):
    body: str = ""
    notebook: str | None = None
    attachments: list[Attachment] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)
```

---

## `src\unobit\models\tag.py`

```python

```

---

## `src\unobit\models\task.py`

```python

```

---

## `src\unobit\pipeline\base.py`

```python
from abc import ABC, abstractmethod

from unobit.core.context import PipelineContext


class PipelineStep(ABC):

    @abstractmethod
    def run(self, notes, context: PipelineContext):
        ...
```

---

## `src\unobit\processors\attachments.py`

```python

```

---

## `src\unobit\processors\base.py`

```python
from typing import Protocol


class Processor(Protocol):
    def process(self, item: object) -> object:
        ...
```

---

## `src\unobit\processors\content_cleanup_processor.py`

```python
class ContentCleanupProcessor:
    def process(self, item: object) -> object:
        body = getattr(item, "body", None)

        if isinstance(body, str):
            item.body = body.strip()

        return item
```

---

## `src\unobit\processors\evernote_internal_link_processor.py`

```python
import re

from unobit.core.context import PipelineContext


class EvernoteInternalLinkProcessor:
    def process_all(self, items: list[object], context: PipelineContext) -> list[object]:
        guid_to_title = self._build_guid_to_title(items)

        for item in items:
            body = getattr(item, "body", None)

            if not isinstance(body, str):
                continue

            item.body = self._replace_links(body, guid_to_title, context)

        return items

    def _build_guid_to_title(self, items: list[object]) -> dict[str, str]:
        guid_to_title: dict[str, str] = {}

        for item in items:
            metadata = getattr(item, "metadata", {}) or {}
            guid = metadata.get("guid")
            title = getattr(item, "title", None)

            if guid and title:
                guid_to_title[str(guid)] = str(title)

        return guid_to_title

    def _replace_links(
        self,
        body: str,
        guid_to_title: dict[str, str],
        context: PipelineContext,
    ) -> str:
        pattern = re.compile(
            r"\[([^\]]+)\]\(evernote:///view/[^)]*?/([a-fA-F0-9-]{32,36})/[^)]*?\)"
        )

        def replace(match: re.Match) -> str:
            label = match.group(1)
            target_guid = match.group(2)

            target_title = guid_to_title.get(target_guid)

            if not target_title:
                context.report.add_warning(
                    "Unresolved Evernote internal link",
                    code="evernote-link-unresolved",
                    target_guid=target_guid,
                    label=label,
                )
                return match.group(0)

            if label and label != target_title:
                return f"[[{target_title}|{label}]]"

            return f"[[{target_title}]]"

        return pattern.sub(replace, body)
```

---

## `src\unobit\processors\markdown.py`

```python

```

---

## `src\unobit\processors\title_cleanup_processor.py`

```python
class TitleCleanupProcessor:
    def process(self, item: object) -> object:
        title = getattr(item, "title", None)

        if isinstance(title, str):
            item.title = title.strip()

        return item
```

---

## `src\unobit\processors\wikilinks.py`

```python

```

---

## `src\unobit\processors\yaml.py`

```python

```

---

## `src\unobit\reporters\__init__.py`

```python

```

---

## `src\unobit\reporters\html_report.py`

```python
from pathlib import Path

from unobit.core.report import ImportReport


class HtmlReportWriter:
    def write(self, report: ImportReport, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)

        html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>UNOBIT Import Report</title>
</head>
<body>
  <h1>UNOBIT Import Report</h1>

  <h2>Summary</h2>
  <ul>
    <li>Importer: {report.importer}</li>
    <li>Source: {report.source}</li>
    <li>Notes imported: {report.notes_total}</li>
    <li>Notes exported: {report.notes_success}</li>
    <li>Warnings: {len(report.warnings)}</li>
    <li>Errors: {len(report.errors)}</li>
  </ul>

  <h2>Attachments</h2>
  <ul>
    <li>Total: {report.attachments_total}</li>
    <li>Exported: {report.attachments_exported}</li>
    <li>Failed: {report.attachments_failed}</li>
  </ul>

  <h2>Media</h2>
  <ul>
    <li>Total: {report.media_total}</li>
    <li>Resolved: {report.media_resolved}</li>
    <li>Unresolved: {report.media_unresolved}</li>
  </ul>

  <h2>Performance</h2>
  <ul>
    <li>Notes/sec: {report.notes_per_second:.2f}</li>
    <li>Attachments/sec: {report.attachments_per_second:.2f}</li>
    <li>Peak memory MB: {report.peak_memory_mb}</li>
  </ul>
</body>
</html>
"""

        path.write_text(html, encoding="utf-8")
```

---

## `src\unobit\reporters\json_report.py`

```python
import json
from pathlib import Path

from unobit.core.report import ImportReport


class JsonReportWriter:
    def write(self, report: ImportReport, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)

        path.write_text(
            json.dumps(
                report,
                default=lambda value: getattr(value, "__dict__", str(value)),
                indent=2,
            ),
            encoding="utf-8",
        )
```

---

## `src\unobit\resolvers\__init__.py.py`

```python

```

---

## `src\unobit\resolvers\attachment_index.py`

```python
from unobit.models import Attachment, Note


class AttachmentIndex:
    def __init__(self, items: list[object]) -> None:
        self.by_checksum: dict[str, Attachment] = {}

        for item in items:
            if not isinstance(item, Note):
                continue

            for attachment in item.attachments:
                if attachment.checksum:
                    self.by_checksum[attachment.checksum.lower()] = attachment

    def get_by_checksum(self, checksum: str | None) -> Attachment | None:
        if not checksum:
            return None

        return self.by_checksum.get(checksum.lower())
```

---

## `src\unobit\resolvers\base.py`

```python
from typing import Protocol

from unobit.core.context import PipelineContext


class Resolver(Protocol):

    def resolve(
        self,
        items: list[object],
        context: PipelineContext,
    ) -> list[object]:
        ...
```

---

## `src\unobit\resolvers\evernote_links.py`

```python
import re

from unobit.core.context import PipelineContext


class EvernoteInternalLinkResolver:
    def resolve(self, items: list[object], context: PipelineContext) -> list[object]:
        guid_to_title = self._build_guid_to_title(items)

        for item in items:
            body = getattr(item, "body", None)

            if not isinstance(body, str):
                continue

            item.body = self._replace_links(body, guid_to_title, context)

        return items

    def _build_guid_to_title(self, items: list[object]) -> dict[str, str]:
        guid_to_title: dict[str, str] = {}

        for item in items:
            metadata = getattr(item, "metadata", {}) or {}
            guid = metadata.get("guid")
            title = getattr(item, "title", None)

            if guid and title:
                guid_to_title[str(guid)] = str(title)

        return guid_to_title

    def _replace_links(
        self,
        body: str,
        guid_to_title: dict[str, str],
        context: PipelineContext,
    ) -> str:
        pattern = re.compile(
            r"\[([^\]]+)\]\(evernote:///view/[^)]*?/([a-fA-F0-9-]{32,36})/[^)]*?\)"
        )

        def replace(match: re.Match) -> str:
            label = match.group(1)
            target_guid = match.group(2)

            target_title = guid_to_title.get(target_guid)

            if not target_title:
                context.report.add_warning(
                    "Unresolved Evernote internal link",
                    code="evernote-link-unresolved",
                    target_guid=target_guid,
                    label=label,
                )
                return match.group(0)

            if label and label != target_title:
                return f"[[{target_title}|{label}]]"

            return f"[[{target_title}]]"

        return pattern.sub(replace, body)
```

---

## `src\unobit\resolvers\media_links.py`

```python
import re

from unobit.core.context import PipelineContext
from unobit.models import Attachment
from unobit.resolvers.attachment_index import AttachmentIndex


class MediaLinkResolver:
    PLACEHOLDER_PATTERN = re.compile(
        r"\[UNOBIT-MEDIA:(\d+):([^:\]]+):([^\]]*)\]"
    )

    def resolve(self, items: list[object], context: PipelineContext) -> list[object]:
        index = AttachmentIndex(items)

        for item in items:
            body = getattr(item, "body", None)

            if not isinstance(body, str):
                continue

            item.body = self._replace_media_links(body, index, context)

        return items

    def _replace_media_links(
        self,
        body: str,
        index: AttachmentIndex,
        context: PipelineContext,
    ) -> str:
        def replace(match: re.Match) -> str:
            media_index = match.group(1)
            media_type = match.group(2)
            checksum = match.group(3)

            context.report.media_total += 1

            attachment = index.get_by_checksum(checksum)

            if attachment is None:
                context.report.media_unresolved += 1
                context.report.add_warning(
                    "Unresolved Evernote media reference",
                    code="evernote-media-unresolved",
                    media_index=media_index,
                    media_type=media_type,
                    checksum=checksum,
                )
                return match.group(0)

            context.report.media_resolved += 1

            return self._to_obsidian_link(attachment)

        return self.PLACEHOLDER_PATTERN.sub(replace, body)

    def _to_obsidian_link(self, attachment: Attachment) -> str:
        path = f"Attachments/{attachment.filename}"
        mime_type = attachment.mime_type or ""

        if mime_type.startswith(("image/", "audio/", "video/")):
            return f"![[{path}]]"

        if mime_type == "application/pdf":
            return f"[[{path}]]"

        return f"[{attachment.filename}]({path})"
```

---

## `src\unobit\services\__init__.py`

```python

```

---

## `src\unobit\services\import_service.py`

```python
from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.performance import MemoryMonitor
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport
from unobit.exporters import MarkdownExporter
from unobit.importers.evernote import EvernoteImporter
from unobit.reporters.html_report import HtmlReportWriter
from unobit.reporters.json_report import JsonReportWriter


def run_evernote_import(
    path: str | Path,
    output: str | Path = "output/evernote",
    language: str = "en",
    json_report: bool = True,
    html_report: bool = False,
) -> ImportReport:
    """Import an Evernote ENEX archive and return its import report."""

    import_path = Path(path)
    output_path = Path(output)

    importer = EvernoteImporter()

    if not import_path.exists():
        raise ValueError(f"Source file not found: {import_path}")

    if not importer.supports_file(import_path):
        raise ValueError(f"Unsupported file: {import_path}")

    report = ImportReport(
        source=str(import_path),
        importer=importer.source_name,
    )

    monitor = MemoryMonitor()
    monitor.start()

    try:
        context = PipelineContext(
            source_path=import_path,
            output_path=output_path,
            importer_name=importer.source_name,
            report=report,
            options={
                "language": language,
                "json_report": json_report,
                "html_report": html_report,
            },
        )

        items = importer.import_file(import_path)
        report.notes_total = len(items)

        pipeline = PipelineFactory.create_default()
        processed_items = pipeline.run(items, context)

        exporter = MarkdownExporter(language=language)

        created_files = exporter.export_items(
            processed_items,
            output_path,
        )

        report.notes_success = len(created_files)
        report.notes_failed = (
            report.notes_total - report.notes_success
        )

        report.attachments_total = sum(
            len(getattr(item, "attachments", []))
            for item in processed_items
        )

        report.attachments_exported = report.attachments_total

        report.finish()
        report.calculate_statistics()

    finally:
        report.peak_memory_mb = monitor.stop()

    if json_report:
        JsonReportWriter().write(
            report,
            output_path / "import-report.json",
        )

    if html_report:
        HtmlReportWriter().write(
            report,
            output_path / "import-report.html",
        )

    return report
```

---

## `src\unobit\utils\__init__.py`

```python

```

---

## `src\unobit\utils\dates.py`

```python
from datetime import datetime


def parse_evernote_datetime(value: str | None) -> datetime | None:
    if not value:
        return None

    try:
        return datetime.strptime(value, "%Y%m%dT%H%M%SZ")
    except ValueError:
        return None


def format_datetime(value: datetime | None) -> str | None:
    if value is None:
        return None

    return value.isoformat()
```

---

## `src\unobit\validators\attachment_validator.py`

```python
from unobit.validators.base import ValidationMessage, ValidationResult


class AttachmentValidator:
    def validate(self, item: object) -> ValidationResult:
        messages: list[ValidationMessage] = []

        attachments = getattr(item, "attachments", None)

        if attachments is None:
            return ValidationResult(messages=[])

        for attachment in attachments:
            filename = getattr(attachment, "filename", None)

            if not filename or not str(filename).strip():
                messages.append(
                    ValidationMessage(
                        level="warning",
                        code="attachment-missing-filename",
                        message="Attachment has no filename",
                    )
                )

        return ValidationResult(messages=messages)
```

---

## `src\unobit\validators\base.py`

```python
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class ValidationMessage:
    level: str
    code: str
    message: str
    context: dict[str, Any] | None = None


@dataclass
class ValidationResult:
    messages: list[ValidationMessage]

    @property
    def has_errors(self) -> bool:
        return any(message.level == "error" for message in self.messages)

    @property
    def has_warnings(self) -> bool:
        return any(message.level == "warning" for message in self.messages)


class Validator(Protocol):
    def validate(self, item: object) -> ValidationResult:
        ...
```

---

## `src\unobit\validators\link_validator.py`

```python

```

---

## `src\unobit\validators\metadata_validator.py`

```python
from unobit.validators.base import ValidationMessage, ValidationResult


class MetadataValidator:
    def validate(self, item: object) -> ValidationResult:
        messages: list[ValidationMessage] = []

        metadata = getattr(item, "metadata", None)

        if metadata is None:
            messages.append(
                ValidationMessage(
                    level="warning",
                    code="note-missing-metadata",
                    message="Note has no metadata",
                )
            )

        return ValidationResult(messages=messages)
```

---

## `src\unobit\validators\note_validator.py`

```python
from unobit.validators.base import ValidationMessage, ValidationResult


class NoteValidator:
    def validate(self, item) -> ValidationResult:
        messages: list[ValidationMessage] = []

        title = getattr(item, "title", None)
        body = getattr(item, "body", None)

        if not title or not str(title).strip():
            messages.append(
                ValidationMessage(
                    level="warning",
                    code="note-missing-title",
                    message="Note has no title",
                )
            )

        if body is None:
            messages.append(
                ValidationMessage(
                    level="error",
                    code="note-missing-body",
                    message="Note has no body",
                )
            )

        return ValidationResult(messages=messages)
```

---
