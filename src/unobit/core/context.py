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