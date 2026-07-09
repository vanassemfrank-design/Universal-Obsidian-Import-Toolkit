from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_FILE = ROOT / "docs" / "bundle_sprint4_context.md"

CONTEXT_FILES = [
    "README.md",
    "CHANGELOG.md",
    "ROADMAP.md",
    "Project-state.md",
    "session-handover.md",
    "docs/architecture.md",
    "docs/architecture-overview.md",
    "docs/user-guide.md",
    "docs/developer-guide.md",
    "docs/public-beta-checklist.md",
]


def read_optional(path: Path) -> str:
    if not path.exists():
        return "_File not found yet._"

    return path.read_text(encoding="utf-8").strip()


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        "# UNOBIT Sprint 4 Context Bundle",
        "",
        f"Generated: {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Sprint 4 Focus",
        "",
        "- CLI uitbreiden",
        "- `unobit.yaml` configuratiebestand",
        "- HTML/JavaScript GUI",
        "- user-guide.md",
        "- developer-guide.md",
        "- public beta voorbereiding",
        "",
        "---",
        "",
    ]

    for relative in CONTEXT_FILES:
        path = ROOT / relative
        lines.extend(
            [
                f"# File: `{relative}`",
                "",
                read_optional(path),
                "",
                "---",
                "",
            ]
        )

    adr_dir = ROOT / "docs" / "adr"
    if adr_dir.exists():
        lines.extend(["# ADR Files", "", "---", ""])

        for adr in sorted(adr_dir.glob("*.md")):
            rel = adr.relative_to(ROOT)
            lines.extend(
                [
                    f"# File: `{rel}`",
                    "",
                    read_optional(adr),
                    "",
                    "---",
                    "",
                ]
            )

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Written: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()