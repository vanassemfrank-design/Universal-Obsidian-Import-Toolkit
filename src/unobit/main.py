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


if __name__ == "__main__":
    app()