from unobit.exporters import MarkdownExporter
from pathlib import Path
from unobit.importers import DummyImporter
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


if __name__ == "__main__":
    app()