import json
from typing import Any

import requests

from src.decorators import retry
from src.my_logger import logger


def get_transactions(filepath: str) -> Any:
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


@retry(3)
def get_actual_currency(currency: str) -> Any:
    """
    Получает актуальный курс валюты из внешнего источника.

    :param currency: Код валюты (например, "RUB").
    :return: Актуальный курс валюты.
    """
    try:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        if response.status_code == 200:
            currency_info = response.json()
            return currency_info["Valute"][currency]["Value"]
        return []

    except KeyError:
        logger.warning('Функция работает только с "RUB", "USD" и "EUR"')
        return 'KeyError: Функция работает только с "RUB", "USD" и "EUR"'

    except Exception as ex:
        error = f"{ex.__class__.__name__}: {ex}"
        logger.error(error)
        return error
