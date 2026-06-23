from pathlib import Path
from datetime import datetime
import csv


LOG_FOLDER = Path("logs")


def ensure_logs_folder() -> None:
    LOG_FOLDER.mkdir(
        exist_ok=True
    )


def create_log_file() -> Path:

    ensure_logs_folder()

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    file_path = (
        LOG_FOLDER /
        f"run_{timestamp}.csv"
    )

    with open(
        file_path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "phone",
            "status"
        ])

    return file_path


def log_row(
    log_path: Path,
    phone: str,
    status: str
) -> None:

    with open(
        log_path,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            phone,
            status
        ])