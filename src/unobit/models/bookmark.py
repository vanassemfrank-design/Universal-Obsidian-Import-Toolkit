from dataclasses import dataclass

from unobit.models.knowledge_item import KnowledgeItem


@dataclass
class Bookmark(KnowledgeItem):
    url: str = ""
    folder: str | None = None
    description: str | None = None