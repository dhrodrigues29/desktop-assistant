import pyperclip


def set_clipboard(text: str) -> None:
    pyperclip.copy(text)


def get_clipboard() -> str:
    return pyperclip.paste()