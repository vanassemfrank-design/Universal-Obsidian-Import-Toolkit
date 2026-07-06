from datetime import datetime


def parse_evernote_datetime(value: str | None) -> datetime | None:
    if not value:
        return None

    try:
        return datetime.strptime(value, "%Y%m%dT%H%M%SZ")
    except ValueError:
        return None


def format_datetime(value: datetime | None) -> str | None:
    if value is None:
        return None

    return value.isoformat()