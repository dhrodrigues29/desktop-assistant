import time

from app.config import coordinates, settings
from app.automation import keyboard, mouse, clipboard
from app.data.contacts import load_contacts
from app.message_loader import load_message

from app.logger import (
    create_log_file,
    log_row
)

def prepare_windows() -> None:
    print("Switching to WhatsApp...")
    keyboard.alt_tab(times=2)

    print("Switching to Google Sheets or contact source...")
    keyboard.alt_tab(times=2)


def open_chat_with_number(phone: str) -> None:
    clipboard.set_clipboard(phone)

    keyboard.alt_tab(times=1)
    mouse.click(coordinates.whatsapp_search_bar, settings.delay_seconds)
    keyboard.paste(settings.delay_seconds)

    time.sleep(1)

    mouse.click(coordinates.first_conversation, settings.delay_seconds)


def paste_message(message: str) -> None:
    clipboard.set_clipboard(message)

    mouse.click(coordinates.message_bar, settings.delay_seconds)
    keyboard.paste(settings.delay_seconds)


def run_workflow() -> None:
    contacts = load_contacts(settings.contacts_csv_path)
    message = load_message(settings.message_template_path)
    log_file = create_log_file()
    
    print(f"Loaded {len(contacts)} contacts.")
    print("Type 'ready' to start.")

    command = input("> ").strip().lower()

    if command != "ready":
        print("Canceled.")
        return

    prepare_windows()

    for index, phone in enumerate(contacts, start=1):
        print(f"\nPreparing contact {index}/{len(contacts)}: {phone}")

        open_chat_with_number(phone)
        paste_message(message)

        print("Message pasted. Review it and send manually.")
        input("Press Enter here after sending or skipping this contact...")

        keyboard.alt_tab(times=1)

    print("\nFinished.")