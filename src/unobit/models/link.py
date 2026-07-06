from dataclasses import dataclass


@dataclass
class Link:
    target: str
    label: str | None = None
    is_internal: bool = False
    is_broken: bool = False