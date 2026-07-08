def clean_markdown(markdown: str) -> str:
    markdown = markdown.replace("<en-note>", "")
    markdown = markdown.replace("</en-note>", "")

    lines = [line.rstrip() for line in markdown.splitlines()]
    cleaned = "\n".join(lines).strip()

    return cleaned