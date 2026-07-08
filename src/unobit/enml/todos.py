from bs4 import BeautifulSoup


def convert_todos(soup: BeautifulSoup) -> None:
    for todo in soup.find_all("en-todo"):
        checked = todo.get("checked") == "true"
        replacement = "- [x] " if checked else "- [ ] "
        todo.replace_with(replacement)