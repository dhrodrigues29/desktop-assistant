from dataclasses import dataclass


@dataclass
class Coordinates:
    first_sheet_cell: tuple[int, int] = (300, 220)
    whatsapp_search_bar: tuple[int, int] = (220, 180)
    first_conversation: tuple[int, int] = (250, 300)
    message_bar: tuple[int, int] = (600, 950)


@dataclass
class Settings:
    message_template_path: str = "templates/default.txt"
    delay_seconds: float = 0.7
    contacts_csv_path: str = "data/contacts.csv"
    manual_send: bool = True


coordinates = Coordinates()
settings = Settings()