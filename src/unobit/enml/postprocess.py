import re


def clean_markdown(markdown: str) -> str:
    markdown = markdown.replace("<en-note>", "")
    markdown = markdown.replace("</en-note>", "")

    lines = [line.rstrip() for line in markdown.splitlines()]

    markdown = "\n".join(lines)

    markdown = re.sub(r"\n{3,}", "\n\n", markdown)

    markdown = re.sub(r"[ \t]+$", "", markdown, flags=re.MULTILINE)

    return markdown.strip()