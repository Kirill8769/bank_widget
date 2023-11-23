import json
from typing import Any

import pandas as pd

from src.external_api import get_actual_currency
from src.my_logger import logger


def get_transactions_from_file(filepath: str, csv_delimiter: str = ",") -> Any:
    """
    Читает транзакции из файла JSON и возвращает их в виде списка.

    :param filepath: Путь к файлу с транзакциями.
    :return: Список транзакций.
    """
    try:
        transactions = []
        format_file = filepath[-4:]
        if "json" in format_file:
            with open(filepath, "r", encoding="UTF-8") as file:
                transactions = json.load(file)
        elif "csv" in format_file:
            df = pd.read_csv(filepath, delimiter=csv_delimiter, encoding="UTF-8")
            transactions = df.to_json(orient="records", force_ascii=False)
        elif "xlsx" in format_file:
            df = pd.read_excel(filepath)
            transactions = df.to_json(orient="records", force_ascii=False)
        else:
            logger.warning("Поддерживаются только следующие форматы файлов: json, csv, xlsx")
    except FileNotFoundError as file_ex:
        logger.error(f"{file_ex.__class__.__name__}: {file_ex}")
    except TypeError:
        logger.warning("TypeError: Принимается только строковый формат пути к обрабатываемому файлу")
    except Exception as ex:
        logger.debug(f"{ex.__class__.__name__}: {ex}")
    finally:
        return transactions


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
