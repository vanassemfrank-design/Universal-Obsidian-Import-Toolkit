from pathlib import Path

OUTPUT = Path("docs/code-context/sprint3-evernote-context.md")

FILES = [
    "src/unobit/core/report.py",
    "src/unobit/core/context.py",
    "src/unobit/core/pipeline.py",
    "src/unobit/core/pipeline_factory.py",
    "src/unobit/core/validation_step.py",
    "src/unobit/core/processing_step.py",
    "src/unobit/core/timing_step.py",

    "src/unobit/validators/base.py",
    "src/unobit/validators/note_validator.py",
    "src/unobit/validators/attachment_validator.py",
    "src/unobit/validators/metadata_validator.py",

    "src/unobit/processors/base.py",
    "src/unobit/processors/title_cleanup_processor.py",
    "src/unobit/processors/content_cleanup_processor.py",

    "src/unobit/models/note.py",
    "src/unobit/models/attachment.py",

    "src/unobit/importers/evernote",
    "src/unobit/exporters",
    "src/unobit/cli",
]

def iter_files() -> list[Path]:
    result: list[Path] = []

    for item in FILES:
        path = Path(item)

        if path.is_dir():
            result.extend(sorted(path.rglob("*.py")))
        elif path.is_file():
            result.append(path)

    return result


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    files = iter_files()

    with OUTPUT.open("w", encoding="utf-8") as out:
        out.write("# UNOBIT Sprint 3 Code Context\n\n")
        out.write("> Relevant source files for Evernote Production Ready sprint.\n\n")

        for file in files:
            out.write(f"## `{file.as_posix()}`\n\n")
            out.write("```python\n")
            out.write(file.read_text(encoding="utf-8"))
            out.write("\n```\n\n")

    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()