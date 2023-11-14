import json
import os

from src.decorators import log

#@log("mylog.log")
def get_transactions(filepath: str) -> list[dict]:
    try:
        with open(filepath, "r", encoding="UTF-8") as file:
            transactions = json.load(file)
            print(transactions)
            return transactions
    except:
        print('error')
        return []


def get_sum_transaction(transaction):
    currency = transaction["operationAmount"]["currency"]["code"]
    result = transaction["operationAmount"]["amount"]
    print(currency, result)


path_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath = os.path.join(path_project, "data", "operations.json") #  operations    test


transactions = get_transactions(filepath)

for tr in transactions:
    get_sum_transaction(tr)
