import logging
import os
from datetime import datetime


def log_messages(levelname: str, message: str, *, file_entry: bool = True, console_entry: bool = True) -> None:
    logger = logging.getLogger("log_messages")
    logger.setLevel("INFO")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    if file_entry:
        file_name = datetime.now().strftime("%Y-%m-%d.log")
        file_path = os.path.join(os.path.dirname(__file__), file_name)
        file_handler = logging.FileHandler(filename=file_path, encoding="UTF-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    if console_entry:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if levelname == "info":
        logger.info(message)
    elif levelname == "warning":
        logger.warning(message)
    else:
        logger.error(message)

    if file_entry:
        logger.removeHandler(file_handler)
    if console_entry:
        logger.removeHandler(console_handler)


log_messages("info", "Это информационное сообщение.", file_entry=False)
log_messages("warning", "Это предупреждение.", console_entry=False)
log_messages("error", "Это ошибка.")
