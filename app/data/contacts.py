import csv


def load_contacts(csv_path: str) -> list[str]:
    contacts: list[str] = []

    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            phone = row.get("phone", "").strip()

            if phone:
                contacts.append(phone)

    return contacts