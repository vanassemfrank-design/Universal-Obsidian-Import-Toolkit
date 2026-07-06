import typer

from unobit import __version__

app = typer.Typer(
    help="Universal Obsidian Import Toolkit"
)


@app.command()
def info():

    print()

    print("Universal Obsidian Import Toolkit")

    print("UNOBIT")

    print(f"Version {__version__}")

    print()


@app.command()
def version():

    print(__version__)


if __name__ == "__main__":

    app()