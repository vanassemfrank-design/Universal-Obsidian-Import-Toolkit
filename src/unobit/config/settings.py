from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass
class UnobitSettings:
    output: str = "output/evernote"
    language: str = "en"
    json_report: bool = True
    html_report: bool = False


def load_settings(path: str | Path = "unobit.yaml") -> UnobitSettings:
    config_path = Path(path)

    if not config_path.exists():
        return UnobitSettings()

    data: dict[str, Any] = yaml.safe_load(
        config_path.read_text(encoding="utf-8")
    ) or {}

    return UnobitSettings(
        output=data.get("output", "output/evernote"),
        language=data.get("language", "en"),
        json_report=data.get("json_report", True),
        html_report=data.get("html_report", False),
    )


def write_default_settings(path: str | Path = "unobit.yaml") -> Path:
    config_path = Path(path)

    if config_path.exists():
        return config_path

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