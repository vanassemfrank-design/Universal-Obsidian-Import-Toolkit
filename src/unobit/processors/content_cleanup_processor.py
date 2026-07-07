class ContentCleanupProcessor:
    def process(self, item: object) -> object:
        content = getattr(item, "content", None)

        if isinstance(content, str):
            item.content = content.strip()

        return item