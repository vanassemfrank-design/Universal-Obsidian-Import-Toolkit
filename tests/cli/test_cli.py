from pathlib import Path

from typer.testing import CliRunner

from unobit.main import app


runner = CliRunner()


def test_info_command() -> None:
    result = runner.invoke(app, ["info"])

    assert result.exit_code == 0
    assert "Universal Obsidian Import Toolkit" in result.stdout


def test_version_command() -> None:
    result = runner.invoke(app, ["version"])

    assert result.exit_code == 0
    assert result.stdout.strip()


def test_config_init_creates_file(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "unobit.yaml"

    result = runner.invoke(
        app,
        [
            "config",
            "init",
            str(config_path),
        ],
    )

    assert result.exit_code == 0
    assert config_path.exists()
    assert "Configuration created" in result.stdout


def test_config_show_displays_settings(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "unobit.yaml"

    config_path.write_text(
        "\n".join(
            [
                "output: output/test",
                "language: nl",
                "json_report: true",
                "html_report: true",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "config",
            "show",
            str(config_path),
        ],
    )

    assert result.exit_code == 0
    assert "output/test" in result.stdout
    assert "Language" in result.stdout
    assert "nl" in result.stdout


def test_config_show_rejects_invalid_config(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "unobit.yaml"

    config_path.write_text(
        'language: "de"\n',
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "config",
            "show",
            str(config_path),
        ],
    )

    assert result.exit_code == 2
    assert "Configuration error" in result.stdout
    assert "Unsupported language" in result.stdout


def test_report_show_rejects_missing_file(
    tmp_path: Path,
) -> None:
    missing_path = tmp_path / "missing.json"

    result = runner.invoke(
        app,
        [
            "report",
            "show",
            str(missing_path),
        ],
    )

    assert result.exit_code == 1
    assert "Report not found" in result.stdout


def test_report_show_displays_json_report(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "import-report.json"

    report_path.write_text(
        """
{
  "source": "example.enex",
  "importer": "evernote",
  "notes_total": 2,
  "notes_success": 2,
  "notes_failed": 0,
  "attachments_total": 1,
  "attachments_exported": 1,
  "attachments_failed": 0,
  "media_total": 1,
  "media_resolved": 1,
  "media_unresolved": 0,
  "warnings": [],
  "errors": []
}
""".strip(),
        encoding="utf-8",
    )

    result = runner.invoke(
        app,
        [
            "report",
            "show",
            str(report_path),
        ],
    )

    assert result.exit_code == 0
    assert "UNOBIT Report" in result.stdout
    assert "example.enex" in result.stdout
    assert "Imported" in result.stdout
    assert "2" in result.stdout


def test_import_command_group_exists() -> None:
    result = runner.invoke(
        app,
        [
            "import",
            "--help",
        ],
    )

    assert result.exit_code == 0
    assert "evernote" in result.stdout


def test_gui_command_group_exists() -> None:
    result = runner.invoke(
        app,
        [
            "gui",
            "--help",
        ],
    )

    assert result.exit_code == 0
    assert "start" in result.stdout