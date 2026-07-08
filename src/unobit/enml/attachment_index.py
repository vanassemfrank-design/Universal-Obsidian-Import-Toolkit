from unobit.models import Attachment, Note


class AttachmentIndex:
    def __init__(self, notes: list[Note]) -> None:
        self.by_hash: dict[str, Attachment] = {}

        for note in notes:
            for attachment in note.attachments:
                if attachment.checksum:
                    self.by_hash[attachment.checksum.lower()] = attachment

    def get(self, checksum: str):
        return self.by_hash.get(checksum.lower())