from unobit.models import Attachment, Note


class AttachmentIndex:
    def __init__(self, items: list[object]) -> None:
        self.by_checksum: dict[str, Attachment] = {}

        for item in items:
            if not isinstance(item, Note):
                continue

            for attachment in item.attachments:
                if attachment.checksum:
                    self.by_checksum[attachment.checksum.lower()] = attachment

    def get_by_checksum(self, checksum: str | None) -> Attachment | None:
        if not checksum:
            return None

        return self.by_checksum.get(checksum.lower())