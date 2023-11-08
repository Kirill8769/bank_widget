import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.test_data import transactions


@pytest.fixture()
def get_transactions():
    return transactions


def test_filter_by_currency_correct(get_transactions):
    result = list(filter_by_currency(get_transactions, "USD"))
    assert len(result) == 3
    assert all(transaction["operationAmount"]["currency"]["name"] == "USD" for transaction in result)


def test_transaction_descriptions_correct(get_transactions):
    result = list(transaction_descriptions(get_transactions))
    assert len(result) == 5


@pytest.mark.parametrize("start, stop, expected", [(1, 5, 5), (55, 100, 46)])
def test_card_number_generator_correct(start, stop, expected):
    result = list(card_number_generator(start, stop))
    assert len(result) == expected
