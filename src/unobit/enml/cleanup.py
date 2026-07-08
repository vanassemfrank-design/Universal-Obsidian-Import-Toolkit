from bs4 import BeautifulSoup


def parse_enml(content: str) -> BeautifulSoup:
    return BeautifulSoup(content, features="xml")


def extract_en_note_html(soup: BeautifulSoup, fallback: str) -> str:
    en_note = soup.find("en-note")

    if en_note:
        return str(en_note)

    return fallback