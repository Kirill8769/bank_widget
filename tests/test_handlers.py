import json
import os

import pytest

from src.handlers import get_filtered_transactions_by_category, get_filtered_transactions_by_search_string


@pytest.fixture()
def transactions_list():
    path_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(path_project, "test_data", "operations.json")
    with open(filepath, encoding="UTF=8") as file:
        transactions = json.load(file)
    return transactions


@pytest.mark.parametrize("search, expected", [("Перевод", 90), ("со счета", 15), ("открытие", 10)])
def test_get_filtered_transactions_by_search_string_correct(transactions_list, search, expected):
    result = get_filtered_transactions_by_search_string(transactions_list, search)
    assert len(result) == expected
    assert all([search.lower() in transaction["description"].lower() for transaction in result])


def test_get_filtered_transactions_by_search_string_incorrect_types(transactions_list):
    assert get_filtered_transactions_by_search_string(transactions_list, 123) == []
    assert get_filtered_transactions_by_search_string(["incorrect_list"], "Перевод") == []
    assert get_filtered_transactions_by_search_string("incorrect_data", "Перевод") == []


def test_get_filtered_transactions_by_category_correct(transactions_list):
    assert get_filtered_transactions_by_category(transactions_list) == {
        "Перевод организации": 40,
        "Открытие вклада": 10,
        "Перевод со счета на счет": 15,
        "Перевод с карты на карту": 19,
        "Перевод с карты на счет": 16,
    }
    assert get_filtered_transactions_by_category(transactions_list, {"Перевод организации": 0}) == {
        "Перевод организации": 40
    }


def test_get_filtered_transactions_by_category_incorrect_types(transactions_list):
    assert get_filtered_transactions_by_category(transactions_list, {}) == {}
    assert get_filtered_transactions_by_category(["incorrect_list"], {}) == {}
    assert get_filtered_transactions_by_category("incorrect_data", {}) == {}
    assert get_filtered_transactions_by_category(transactions_list, {"Перевод организации": "incorrect_type"}) == {}
