from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport
from pathlib import Path
from unobit.importers import DummyImporter, EvernoteImporter
from unobit.exporters import MarkdownExporter
from unobit.services.import_service import run_evernote_import

import typer
from rich import print

from unobit import __version__
from unobit.models import Bookmark, Note

from unobit.core.performance import MemoryMonitor
from unobit.reporters.json_report import JsonReportWriter
from unobit.config.settings import load_settings, write_default_settings


app = typer.Typer(help="Universal Obsidian Import Toolkit")
import_app = typer.Typer(help="Import commands")
config_app = typer.Typer(help="Configuration commands")
report_app = typer.Typer(help="Report commands")
gui_app = typer.Typer(help="GUI commands")

app.add_typer(import_app, name="import")
app.add_typer(config_app, name="config")
app.add_typer(report_app, name="report")
app.add_typer(gui_app, name="gui")


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

@import_app.command("evernote")
def import_evernote(path: str, output: str = "output/evernote"):
    try:
        report = run_evernote_import(path, output)
    except ValueError as error:
        print(f"[red]{error}[/red]")
        raise typer.Exit(code=1)



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

@config_app.command("init")
def config_init(path: str = "unobit.yaml"):
    created_path = write_default_settings(path)
    print(f"[green]Configuration ready:[/green] {created_path}")


@config_app.command("show")
def config_show(path: str = "unobit.yaml"):
    settings = load_settings(path)

    print("[bold]UNOBIT Configuration[/bold]")
    print(f"output      : {settings.output}")
    print(f"language    : {settings.language}")
    print(f"json_report : {settings.json_report}")
    print(f"html_report : {settings.html_report}")