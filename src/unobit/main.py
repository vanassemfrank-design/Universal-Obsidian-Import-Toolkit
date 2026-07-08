from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport
from pathlib import Path
from unobit.importers import DummyImporter, EvernoteImporter
from unobit.exporters import MarkdownExporter

import typer
from rich import print

from unobit import __version__
from unobit.models import Bookmark, Note

app = typer.Typer(help="Universal Obsidian Import Toolkit")


@app.command()
def info():
    print()
    print("[bold]Universal Obsidian Import Toolkit[/bold]")
    print("UNOBIT")
    print(f"Version {__version__}")
    print()


@app.command()
def version():
    print(__version__)


@app.command()
def demo():
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
def import_dummy(path: str = "samples/dummy/example.dummy"):
    importer = DummyImporter()
    import_path = Path(path)

    if not importer.supports_file(import_path):
        print(f"[red]Unsupported file:[/red] {import_path}")
        raise typer.Exit(code=1)

    items = importer.import_file(import_path)

    print(f"[bold]Imported {len(items)} items from {import_path}[/bold]")
    print()

    for item in items:
        print(item)
        print()

@app.command()
def export_demo(output: str = "output/demo"):
    note = Note(
        title="Example Evernote Note",
        source="evernote",
        notebook="Inbox",
        body="This is a universal note object exported to Markdown.",
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
    created_files = exporter.export_items([note, bookmark], Path(output))

    print(f"[bold]Exported {len(created_files)} files to {output}[/bold]")
    print()

    for file_path in created_files:
        print(file_path)

@app.command()
def import_evernote(path: str, output: str = "output/evernote"):
    import_path = Path(path)
    output_path = Path(output)

    importer = EvernoteImporter()

    if not importer.supports_file(import_path):
        print(f"[red]Unsupported file:[/red] {import_path}")
        raise typer.Exit(code=1)

    report = ImportReport(
        source=str(import_path),
        importer=importer.source_name,
    )

    context = PipelineContext(
        source_path=import_path,
        output_path=output_path,
        importer_name=importer.source_name,
        report=report,
    )

    items = importer.import_file(import_path)
    report.notes_total = len(items)

    pipeline = PipelineFactory.create_default()
    processed_items = pipeline.run(items, context)

    exporter = MarkdownExporter()
    created_files = exporter.export_items(processed_items, output_path)

    report.notes_success = len(created_files)
    report.notes_failed = report.notes_total - report.notes_success

    report.attachments_total = sum(
        len(getattr(item, "attachments", []))
        for item in processed_items
    )
    report.attachments_exported = report.attachments_total

    report.finish()

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
    print(f"Warnings     : {len(report.warnings)}")
    print(f"Errors       : {len(report.errors)}")

    if report.timings:
        print()
        print("Timings")
        for name, seconds in report.timings.items():
            print(f"  {name:<12}: {report.format_duration(seconds)}")
    
    if report.duration_seconds is not None:
        print()
        print(f"Total time   : {report.format_duration(report.duration_seconds)}")

    print()
    print(f"Output       : {output_path}")
    print("------------------------------------")

@app.command()
def debug_evernote(path: str):
    import_path = Path(path)
    importer = EvernoteImporter()

    items = importer.import_file(import_path)

    print(f"[bold]Debug Evernote import[/bold]")
    print(f"File: {import_path}")
    print(f"Items: {len(items)}")
    print()

    for item in items:
        attachment_count = len(getattr(item, "attachments", []))
        print(f"- {item.title}")
        print(f"  attachments: {attachment_count}")

        for attachment in getattr(item, "attachments", []):
            print(f"    - filename: {attachment.filename}")
            print(f"      mime: {attachment.mime_type}")
            print(f"      checksum: {attachment.checksum}")
            print(f"      size: {attachment.size_bytes}")

