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