LABELS = {
    "en": {
        "attachments": "Attachments",
    },
    "nl": {
        "attachments": "Bijlagen",
    },
}


def get_label(key: str, language: str = "en") -> str:
    return LABELS.get(language, LABELS["en"]).get(key, key)