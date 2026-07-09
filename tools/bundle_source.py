from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "src" / "unobit"
OUTPUT_FILE = ROOT / "docs" / "source-bundle.md"


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(SOURCE_DIR.rglob("*.py"))

    lines = [
        "# UNOBIT Source Bundle",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        f"Source: `{SOURCE_DIR}`",
        "",
        "---",
        "",
        "## Files",
        "",
    ]

    for file in files:
        rel = file.relative_to(ROOT)
        lines.append(f"- `{rel}`")

    lines.extend(["", "---", ""])

    for file in files:
        rel = file.relative_to(ROOT)
        content = file.read_text(encoding="utf-8")

        lines.extend(
            [
                f"## `{rel}`",
                "",
                "```python",
                content.rstrip(),
                "```",
                "",
                "---",
                "",
            ]
        )

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()