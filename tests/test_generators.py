import pytest
from typing import Generator

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator
from src.test_data import transactions

# @pytest.mark.parametrize('transactions_list, currency, expected', [
#     ()
# ])
@pytest.fixture()
def get_transactions():
    return transactions

@pytest.fixture()
def incorrect_data():
    return ["One", True, 3, [1, "hello", [0]], "hi", {}, "", [], False]


def test_filter_by_currency_correct(get_transactions):
    result = list(filter_by_currency(get_transactions, "USD"))
    assert len(result) == 3
    assert all(transaction["operationAmount"]["currency"]["name"] == "USD" for transaction in result)


def test_transaction_descriptions(get_transactions):
    result = list(transaction_descriptions(get_transactions))
    assert len(result) == 5


@pytest.mark.parametrize('start, stop, expected', [
    (1, 5, 5),
    (55, 100, 46)
])
def test_card_number_generator(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert len(result) == expected


def test_incorrect_data(incorrect_data):
    with pytest.raises(Exception):
        transaction_descriptions(incorrect_data)
