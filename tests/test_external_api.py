from unittest.mock import Mock, patch

from src.utils import get_actual_currency, get_amount_transaction

transaction = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702",
}


@patch("src.utils.get_actual_currency")
def test_get_amount_transaction_usd_eur(mock_get_actual_currency):
    mock_get_actual_currency.return_value = 88.9466
    assert get_amount_transaction(transaction) == 88.9466
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
