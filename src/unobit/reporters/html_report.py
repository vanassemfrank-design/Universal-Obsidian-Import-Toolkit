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