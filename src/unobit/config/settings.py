from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


SUPPORTED_LANGUAGES = {"en", "nl"}


class ConfigError(ValueError):
    """Raised when an UNOBIT configuration file is invalid."""


@dataclass
class UnobitSettings:
    output: str = "output/evernote"
    language: str = "en"
    json_report: bool = True
    html_report: bool = False


def load_settings(
    path: str | Path = "unobit.yaml",
) -> UnobitSettings:
    config_path = Path(path)

    if not config_path.exists():
        return UnobitSettings()

    try:
        raw_data = config_path.read_text(encoding="utf-8")
        loaded_data = yaml.safe_load(raw_data)
    except OSError as error:
        raise ConfigError(
            f"Could not read configuration file: {config_path}"
        ) from error
    except yaml.YAMLError as error:
        raise ConfigError(
            f"Invalid YAML in configuration file: {config_path}"
        ) from error

    if loaded_data is None:
        data: dict[str, Any] = {}
    elif isinstance(loaded_data, dict):
        data = loaded_data
    else:
        raise ConfigError(
            "Configuration root must be a YAML object."
        )

    settings = UnobitSettings(
        output=_read_string(
            data,
            key="output",
            default="output/evernote",
        ),
        language=_read_string(
            data,
            key="language",
            default="en",
        ).lower(),
        json_report=_read_boolean(
            data,
            key="json_report",
            default=True,
        ),
        html_report=_read_boolean(
            data,
            key="html_report",
            default=False,
        ),
    )

    validate_settings(settings)

    return settings


def validate_settings(settings: UnobitSettings) -> None:
    if not settings.output.strip():
        raise ConfigError(
            "Configuration value 'output' cannot be empty."
        )

    if settings.language not in SUPPORTED_LANGUAGES:
        supported = ", ".join(sorted(SUPPORTED_LANGUAGES))

        raise ConfigError(
            "Unsupported language "
            f"'{settings.language}'. Supported: {supported}."
        )

    if not settings.json_report and not settings.html_report:
        raise ConfigError(
            "At least one report format must be enabled: "
            "'json_report' or 'html_report'."
        )


def write_default_settings(
    path: str | Path = "unobit.yaml",
) -> Path:
    config_path = Path(path)

    if config_path.exists():
        return config_path

    config_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    config_path.write_text(
        "\n".join(
            [
                "output: output/evernote",
                "language: en",
                "json_report: true",
                "html_report: false",
                "",
            ]
        ),
        encoding="utf-8",
    )

    return config_path


def _read_string(
    data: dict[str, Any],
    key: str,
    default: str,
) -> str:
    value = data.get(key, default)

    if not isinstance(value, str):
        raise ConfigError(
            f"Configuration value '{key}' must be a string."
        )

    return value


def _read_boolean(
    data: dict[str, Any],
    key: str,
    default: bool,
) -> bool:
    value = data.get(key, default)

    if not isinstance(value, bool):
        raise ConfigError(
            f"Configuration value '{key}' must be true or false."
        )

    return value