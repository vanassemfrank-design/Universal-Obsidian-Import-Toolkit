class ContentCleanupProcessor:
    def process(self, item: object) -> object:
        body = getattr(item, "body", None)

        if isinstance(body, str):
            item.body = body.strip()

        return item