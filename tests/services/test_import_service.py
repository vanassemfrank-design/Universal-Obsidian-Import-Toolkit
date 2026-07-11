from pathlib import Path

from unobit.services.import_service import run_evernote_import


PROJECT_ROOT = Path(__file__).resolve().parents[2]

FIXTURE = (
    PROJECT_ROOT
    / "tests"
    / "data"
    / "evernote"
    / "internal-links.enex"
)


def test_import_service_writes_json_report(
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "output"

    report = run_evernote_import(
        path=FIXTURE,
        output=output_path,
        language="en",
        json_report=True,
        html_report=False,
    )

    assert report.notes_total > 0
    assert (output_path / "import-report.json").exists()
    assert not (output_path / "import-report.html").exists()


def test_import_service_writes_html_report(
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "output"

    report = run_evernote_import(
        path=FIXTURE,
        output=output_path,
        language="en",
        json_report=False,
        html_report=True,
    )

    assert report.notes_total > 0
    assert not (output_path / "import-report.json").exists()
    assert (output_path / "import-report.html").exists()


def test_import_service_writes_both_reports(
    tmp_path: Path,
) -> None:
    output_path = tmp_path / "output"

    run_evernote_import(
        path=FIXTURE,
        output=output_path,
        language="nl",
        json_report=True,
        html_report=True,
    )

    assert (output_path / "import-report.json").exists()
    assert (output_path / "import-report.html").exists()


