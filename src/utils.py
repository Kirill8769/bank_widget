import json
import os
from typing import Any

import pandas as pd

from src.external_api import get_actual_currency
from src.my_logger import logger


def get_transactions_from_file(filepath: str, csv_delimiter: str = ",") -> Any:
    """
    Читает транзакции из файла и возвращает их в виде списка.
    Поддерживает форматы JSON, XLS, XLSX, CSV

    :param filepath: Путь к файлу с транзакциями.
    :param csv_delimiter: Разделитель при чтении CSV файла (по умолчанию ",").
    :return: Список транзакций.
    """
    try:
        transactions = []
        if not isinstance(filepath, str):
            raise TypeError("Принимается только строковый формат пути к обрабатываемому файлу")
        if not os.path.isfile(filepath):
            raise FileNotFoundError("Файл не найден")
        format_file = filepath[-4:]
        if "json" in format_file:
            with open(filepath, "r", encoding="UTF-8") as file:
                transactions = json.load(file)
        elif "csv" in format_file:
            df = pd.read_csv(filepath, delimiter=csv_delimiter, encoding="UTF-8")
            transactions = json.loads(df.to_json(orient="records", force_ascii=False))
        elif "xls" in format_file:
            df = pd.read_excel(filepath)
            transactions = json.loads(df.to_json(orient="records", force_ascii=False))
        else:
            logger.warning("Поддерживаются только следующие форматы файлов: json, csv, xlsx")
    except FileNotFoundError as file_ex:
        logger.error(f"{file_ex.__class__.__name__}: {file_ex}")
    except TypeError as type_ex:
        logger.error(f"{type_ex.__class__.__name__}: {type_ex}")
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


def get_result_answer(
        answer: str,
        words_yes: list = ["yes", "y", "да", "д"],
        words_no: list = ["no", "n", "нет", "н"]
):
    pass