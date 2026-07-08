from bs4 import BeautifulSoup


def convert_media_placeholders(soup: BeautifulSoup) -> None:
    for index, media in enumerate(soup.find_all("en-media"), start=1):
        media_type = media.get("type") or "application/octet-stream"
        media_hash = media.get("hash") or ""

        placeholder = f"[UNOBIT-MEDIA:{index}:{media_type}:{media_hash}]"

        media.replace_with(placeholder)