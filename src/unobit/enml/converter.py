from markdownify import markdownify as md
from unobit.enml.media import convert_media_placeholders

from unobit.enml.cleanup import (
    extract_en_note_html,
    normalize_whitespace,
    parse_enml,
    remove_empty_nodes,
)
from unobit.enml.postprocess import clean_markdown
from unobit.enml.todos import convert_todos


class ENMLConverter:
    def convert(self, content: str) -> str:
        soup = parse_enml(content)
        
        remove_empty_nodes(soup)
        normalize_whitespace(soup)
        convert_todos(soup)
        convert_media_placeholders(soup)

        html = extract_en_note_html(soup, fallback=content)

        markdown = md(
            html,
            heading_style="ATX",
            bullets="-",
        )

        return clean_markdown(markdown)