import json
from typing import Any

from src.external_api import get_actual_currency
from src.my_logger import logger


def get_transactions_json(filepath: str) -> Any:
    """
    Читает транзакции из файла JSON и возвращает их в виде списка.

    :param filepath: Путь к файлу с транзакциями.
    :return: Список транзакций.
    """
    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            transactions = json.load(file)
            return transactions
    except Exception as ex:
        logger.error(f"{ex.__class__.__name__}: {ex}")
        return []


def get_amount_transaction(transaction: dict) -> Any:
    """
    Получает транзакцию в виде словаря и возвращает сумму.

    :param transaction: Информация о транзакции.
    :return: Сумма транзакции.
    """
    try:
        currency: str = transaction["operationAmount"]["currency"]["code"]
        amount: str = transaction["operationAmount"]["amount"]
        if currency == "RUB":
            return float(amount)
        elif currency in ["USD", "EUR"]:
            return get_actual_currency(currency)
        message = "Транзакция в указанной валюте не обрабатывается"
        logger.warning(message)
        return ValueError(message)
    except Exception as ex:
        error = f"{ex.__class__.__name__}: {ex}"
        logger.error(error)
        return error
