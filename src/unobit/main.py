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