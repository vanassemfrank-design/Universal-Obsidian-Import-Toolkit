from markdownify import markdownify as md

from unobit.enml.cleanup import extract_en_note_html, parse_enml
from unobit.enml.postprocess import clean_markdown
from unobit.enml.todos import convert_todos


class ENMLConverter:
    def convert(self, content: str) -> str:
        soup = parse_enml(content)

        convert_todos(soup)

        html = extract_en_note_html(soup, fallback=content)

        markdown = md(
            html,
            heading_style="ATX",
            bullets="-",
        )

        return clean_markdown(markdown)