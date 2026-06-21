import time
import pyautogui


def alt_tab(times: int = 1, delay: float = 0.3) -> None:
    for _ in range(times):
        pyautogui.hotkey("alt", "tab")
        time.sleep(delay)


def copy(delay: float = 0.2) -> None:
    pyautogui.hotkey("ctrl", "c")
    time.sleep(delay)


def paste(delay: float = 0.2) -> None:
    pyautogui.hotkey("ctrl", "v")
    time.sleep(delay)


def press_enter(delay: float = 0.2) -> None:
    pyautogui.press("enter")
    time.sleep(delay)