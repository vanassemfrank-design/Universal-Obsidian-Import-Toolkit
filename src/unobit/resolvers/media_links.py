import re

from unobit.core.context import PipelineContext
from unobit.models import Attachment
from unobit.resolvers.attachment_index import AttachmentIndex


class MediaLinkResolver:
    PLACEHOLDER_PATTERN = re.compile(
        r"\[UNOBIT-MEDIA:(\d+):([^:\]]+):([^\]]*)\]"
    )

    def resolve(self, items: list[object], context: PipelineContext) -> list[object]:
        index = AttachmentIndex(items)

        for item in items:
            body = getattr(item, "body", None)

            if not isinstance(body, str):
                continue

            item.body = self._replace_media_links(body, index, context)

        return items

    def _replace_media_links(
        self,
        body: str,
        index: AttachmentIndex,
        context: PipelineContext,
    ) -> str:
        def replace(match: re.Match) -> str:
            media_index = match.group(1)
            media_type = match.group(2)
            checksum = match.group(3)

            context.report.media_total += 1

            attachment = index.get_by_checksum(checksum)

            if attachment is None:
                context.report.media_unresolved += 1
                context.report.add_warning(
                    "Unresolved Evernote media reference",
                    code="evernote-media-unresolved",
                    media_index=media_index,
                    media_type=media_type,
                    checksum=checksum,
                )
                return match.group(0)

            context.report.media_resolved += 1

            return self._to_obsidian_link(attachment)

        return self.PLACEHOLDER_PATTERN.sub(replace, body)

    def _to_obsidian_link(self, attachment: Attachment) -> str:
        path = f"Attachments/{attachment.filename}"
        mime_type = attachment.mime_type or ""

        if mime_type.startswith(("image/", "audio/", "video/")):
            return f"![[{path}]]"

        if mime_type == "application/pdf":
            return f"[[{path}]]"

        return f"[{attachment.filename}]({path})"