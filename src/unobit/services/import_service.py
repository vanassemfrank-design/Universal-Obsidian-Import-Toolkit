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