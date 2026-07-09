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