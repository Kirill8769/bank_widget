import os
from unittest.mock import Mock, patch

import pytest

from src.utils import get_actual_currency, get_amount_transaction, get_transactions

path_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath = os.path.join(path_project, "data", "operations.json")
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


@pytest.fixture
def correct_json_list():
    return transactions


def test_get_transactions_correct_path():
    result = get_transactions(filepath)
    assert isinstance(result, list)
    assert isinstance(result[0], dict)


def test_get_transactions_incorrect_path():
    assert get_transactions("") == []


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


@patch("src.utils.get_actual_currency")
def test_get_amount_transaction_usd_eur(mock_get_actual_currency):
    mock_get_actual_currency.return_value = 88.9466
    assert get_amount_transaction(transactions[2]) == 88.9466
    mock_get_actual_currency.assert_called_once_with("USD")


def test_get_actual_currency_valid():
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"Valute": {"USD": {"Value": 88.9466}}}
        mock_get.return_value = mock_response
        assert get_actual_currency("USD") == 88.9466
        mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")


@patch("requests.get")
def test_get_actual_currency_invalid(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = KeyError("Invalid currency")
    mock_get.return_value = mock_response
    assert get_actual_currency("AUD") == 'KeyError: Функция работает только с "RUB", "USD" и "EUR"'
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")


@patch("requests.get")
def test_get_actual_currency_json_decode_error(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.side_effect = ValueError("Invalid JSON")
    mock_get.return_value = mock_response
    result = get_actual_currency("USD")
    assert result == "ValueError: Invalid JSON"
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")


@patch("requests.get")
def test_get_actual_currency_other_exception(mock_get):
    mock_get.side_effect = Exception("Some error")
    result = get_actual_currency("USD")
    assert result == "Exception: Some error"
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")


@patch("requests.get")
def test_get_actual_currency_invalid_status_code(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    assert get_actual_currency("USD") == []
    mock_get.assert_called_once_with("https://www.cbr-xml-daily.ru/daily_json.js")
