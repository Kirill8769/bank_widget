import os
from unittest.mock import patch

import pytest

from src.utils import get_amount_transaction, get_transactions_from_file

path_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath_json = os.path.join(path_project, "test_data", "operations.json")
filepath_csv = os.path.join(path_project, "test_data", "transactions.csv")
filepath_xlsx = os.path.join(path_project, "test_data", "transactions_excel.xlsx")
filepath_incorrect = os.path.join(path_project, "test_data", "incorrect_file.json")
incorrect_format = os.path.join(path_project, "test_data", "incorrect_format.doc")

transactions = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "AUD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
]


@pytest.mark.parametrize(
    "filepath, delimiter",
    [
        (filepath_json, None),
        (filepath_csv, ";"),
        (filepath_xlsx, None),
    ],
)
@patch("src.utils.get_transactions_from_file")
def test_get_transactions_from_file_correct_return(mock_get_transactions_from_file, filepath, delimiter):
    mock_get_transactions_from_file.return_value = [{"transaction": 1, "message": "ok"}]
    assert mock_get_transactions_from_file() == [{"transaction": 1, "message": "ok"}]
    mock_get_transactions_from_file.assert_called_once_with()
    result = get_transactions_from_file(filepath, delimiter)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)


def test_get_transactions_from_file_incorrect_path():
    assert get_transactions_from_file("") == []
    assert get_transactions_from_file(123) == []


def test_get_transactions_from_file_incorrect_format():
    assert get_transactions_from_file(incorrect_format) == []


def test_get_amount_transaction_rub():
    assert get_amount_transaction(transactions[0]) == 31957.58


def test_get_amount_transaction_other():
    result = get_amount_transaction(transactions[1])
    assert isinstance(result, ValueError)
    assert str(result) == "Транзакция в указанной валюте не обрабатывается"


@pytest.mark.parametrize(
    "transaction, expected", [({"incorrect_key": "value"}, "KeyError"), ("incorrect_type", "TypeError")]
)
def test_get_amount_transaction_key_error(transaction, expected):
    result = get_amount_transaction(transaction)
    assert expected in result
