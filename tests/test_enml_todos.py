from unobit.enml.cleanup import parse_enml
from unobit.enml.todos import convert_todos


def test_convert_todos_replaces_open_todo():
    soup = parse_enml("<en-note><div><en-todo/> Open task</div></en-note>")

    convert_todos(soup)

    assert "- [ ] " in str(soup)


def test_convert_todos_replaces_done_todo():
    soup = parse_enml(
        '<en-note><div><en-todo checked="true"/> Done task</div></en-note>'
    )

    convert_todos(soup)

    assert "- [x] " in str(soup)