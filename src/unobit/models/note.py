from dataclasses import dataclass, field

from unobit.models.attachment import Attachment
from unobit.models.knowledge_item import KnowledgeItem
from unobit.models.link import Link


@dataclass
class Note(KnowledgeItem):
    body: str = ""
    notebook: str | None = None
    attachments: list[Attachment] = field(default_factory=list)
    links: list[Link] = field(default_factory=list)