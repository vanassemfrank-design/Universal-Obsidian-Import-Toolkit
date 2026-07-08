import re

from unobit.core.context import PipelineContext


class EvernoteInternalLinkResolver:
    def resolve(self, items: list[object], context: PipelineContext) -> list[object]:
        guid_to_title = self._build_guid_to_title(items)

        for item in items:
            body = getattr(item, "body", None)

            if not isinstance(body, str):
                continue

            item.body = self._replace_links(body, guid_to_title, context)

        return items

    def _build_guid_to_title(self, items: list[object]) -> dict[str, str]:
        guid_to_title: dict[str, str] = {}

        for item in items:
            metadata = getattr(item, "metadata", {}) or {}
            guid = metadata.get("guid")
            title = getattr(item, "title", None)

            if guid and title:
                guid_to_title[str(guid)] = str(title)

        return guid_to_title

    def _replace_links(
        self,
        body: str,
        guid_to_title: dict[str, str],
        context: PipelineContext,
    ) -> str:
        pattern = re.compile(
            r"\[([^\]]+)\]\(evernote:///view/[^)]*?/([a-fA-F0-9-]{32,36})/[^)]*?\)"
        )

        def replace(match: re.Match) -> str:
            label = match.group(1)
            target_guid = match.group(2)

            target_title = guid_to_title.get(target_guid)

            if not target_title:
                context.report.add_warning(
                    "Unresolved Evernote internal link",
                    code="evernote-link-unresolved",
                    target_guid=target_guid,
                    label=label,
                )
                return match.group(0)

            if label and label != target_title:
                return f"[[{target_title}|{label}]]"

            return f"[[{target_title}]]"

        return pattern.sub(replace, body)