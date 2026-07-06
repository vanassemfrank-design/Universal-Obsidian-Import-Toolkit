from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass
class KnowledgeItem:
    title: str
    source: str
    id: str = field(default_factory=lambda: str(uuid4()))
    created_at: datetime | None = None
    updated_at: datetime | None = None
    tags: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def item_type(self) -> str:
        return self.__class__.__name__.lower()