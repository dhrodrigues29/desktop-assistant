import time
import pyautogui


def click(position: tuple[int, int], delay: float = 0.3) -> None:
    x, y = position
    pyautogui.click(x=x, y=y)
    time.sleep(delay)