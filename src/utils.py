import json
from typing import Any

import requests


def get_transactions(filepath: str) -> Any:
    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            transactions = json.load(file)
            return transactions
    except Exception:
        return []


def get_amount_transaction(transaction: dict) -> float | str | Exception:
    try:
        currency: str = transaction["operationAmount"]["currency"]["code"]
        amount: str = transaction["operationAmount"]["amount"]
        if currency == "RUB":
            return float(amount)
        elif currency in ["USD", "EUR"]:
            return get_actual_currency(currency)
        return ValueError(f"Транзакция в указанной валюте не обрабатывается")
    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"


def get_actual_currency(currency: str) -> Any:
    try:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        if response.status_code == 200:
            currency_info = response.json()
            print(currency_info)
            return currency_info["Valute"][currency]["Value"]
        return []

    except KeyError:
        return f'KeyError: Функция работает только с "RUB", "USD" и "EUR"'

    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"
