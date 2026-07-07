class TitleCleanupProcessor:
    def process(self, item: object) -> object:
        title = getattr(item, "title", None)

        if isinstance(title, str):
            item.title = title.strip()

        return item