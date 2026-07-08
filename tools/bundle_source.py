from pathlib import Path

ROOT = Path("src/unobit")
OUTPUT = Path("docs/code-context/unobit-source-bundle.md")

EXCLUDE_DIRS = {
    "__pycache__",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
}

def should_include(path: Path) -> bool:
    if any(part in EXCLUDE_DIRS for part in path.parts):
        return False

    if path.suffix in EXCLUDE_SUFFIXES:
        return False

    return path.suffix == ".py"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(path for path in ROOT.rglob("*") if path.is_file() and should_include(path))

    with OUTPUT.open("w", encoding="utf-8") as out:
        out.write("# UNOBIT Source Bundle\n\n")
        out.write("> Generated from `src/unobit`.\n\n")

        for file in files:
            relative = file.as_posix()

            out.write(f"## `{relative}`\n\n")
            out.write("```python\n")
            out.write(file.read_text(encoding="utf-8"))
            out.write("\n```\n\n")

    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()