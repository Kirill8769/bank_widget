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
        return ValueError("Транзакция выполнена не в рублях. Укажите транзакцию в рублях")
    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"


def get_actual_currency(currency: str) -> float | list:
    try:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        if response.status_code == 200:
            currency_info = response.json()
            return currency_info["Valute"][currency]["Value"]
        return []
    
    except KeyError:
        return f"KeyError: ..."
    
    except requests.exceptions.JSONDecodeError:
        return f"JSONDecodeError: ..."
    
    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"
    
        
print(get_actual("EUR"))
