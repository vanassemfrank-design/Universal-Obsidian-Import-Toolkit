from pathlib import Path

import pytest

from unobit.config.settings import (
    ConfigError,
    UnobitSettings,
    load_settings,
    validate_settings,
    write_default_settings,
)


def test_load_settings_returns_defaults_when_file_missing(
    tmp_path: Path,
) -> None:
    settings = load_settings(
        tmp_path / "missing.yaml"
    )

    assert settings.output == "output/evernote"
    assert settings.language == "en"
    assert settings.json_report is True
    assert settings.html_report is False


def test_load_settings_reads_yaml(
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
            ]
        ),
        encoding="utf-8",
    )

    settings = load_settings(config_path)

    assert settings.output == "output/test"
    assert settings.language == "nl"
    assert settings.json_report is True
    assert settings.html_report is True


def test_invalid_language_raises_config_error() -> None:
    settings = UnobitSettings(
        language="de",
    )

    with pytest.raises(
        ConfigError,
        match="Unsupported language",
    ):
        validate_settings(settings)


def test_report_values_must_be_boolean(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "unobit.yaml"

    config_path.write_text(
    'json_report: "yes"\n',
    encoding="utf-8",
    )

    with pytest.raises(
        ConfigError,
        match="json_report",
    ):
        load_settings(config_path)


def test_at_least_one_report_must_be_enabled() -> None:
    settings = UnobitSettings(
        json_report=False,
        html_report=False,
    )

    with pytest.raises(
        ConfigError,
        match="At least one report format",
    ):
        validate_settings(settings)


def test_write_default_settings_creates_file(
    tmp_path: Path,
) -> None:
    config_path = tmp_path / "unobit.yaml"

    result = write_default_settings(config_path)

    assert result == config_path
    assert config_path.exists()
    assert "output: output/evernote" in (
        config_path.read_text(encoding="utf-8")
    )