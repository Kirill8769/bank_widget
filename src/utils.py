import json
from typing import Any


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
        return ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"
