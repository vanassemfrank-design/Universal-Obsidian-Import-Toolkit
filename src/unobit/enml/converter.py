from bs4 import BeautifulSoup
from markdownify import markdownify as md


class ENMLConverter:
    def convert(self, content: str) -> str:
        soup = BeautifulSoup(content, features="xml")

        for todo in soup.find_all("en-todo"):
            checked = todo.get("checked") == "true"
            replacement = "- [x] " if checked else "- [ ] "
            todo.replace_with(replacement)

        en_note = soup.find("en-note")
        html = str(en_note) if en_note else content

        markdown = md(
            html,
            heading_style="ATX",
            bullets="-",
        )

        markdown = markdown.replace("<en-note>", "")
        markdown = markdown.replace("</en-note>", "")

        lines = [line.rstrip() for line in markdown.splitlines()]
        cleaned = "\n".join(lines).strip()

        return cleaned