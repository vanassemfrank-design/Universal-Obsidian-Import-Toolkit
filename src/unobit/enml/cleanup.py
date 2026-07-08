from bs4 import BeautifulSoup, Tag


def parse_enml(content: str) -> BeautifulSoup:
    return BeautifulSoup(content, features="xml")


def remove_empty_nodes(soup: BeautifulSoup) -> None:
    """
    Remove empty XML nodes except media/todo/br/hr.
    """

    keep = {
        "en-media",
        "en-todo",
        "br",
        "hr",
    }

    changed = True

    while changed:
        changed = False

        for tag in list(soup.find_all()):
            if not isinstance(tag, Tag):
                continue

            if tag.name in keep:
                continue

            if tag.text.strip():
                continue

            if tag.find():
                continue

            tag.decompose()
            changed = True


def normalize_whitespace(soup: BeautifulSoup) -> None:
    """
    Remove excessive whitespace from text nodes.
    """

    for text in soup.find_all(string=True):
        text.replace_with(" ".join(text.split()))


def extract_en_note_html(
    soup: BeautifulSoup,
    fallback: str,
) -> str:
    en_note = soup.find("en-note")

    if en_note:
        return str(en_note)

    return fallback