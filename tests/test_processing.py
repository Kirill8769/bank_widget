from typing import Any

import pytest

from src.processing import get_list_sorted_date, get_state_dictionary
from src.test_data import test_operation_info


@pytest.fixture
def coll_correct() -> list[dict]:
    return test_operation_info


@pytest.fixture
def coll_uncorrect() -> list:
    return ["One", True, 3, [1, "hello", [0]], "hi", {}, "", [], False]


def test_get_state_dictionary_correct(coll_correct: list) -> None:
    assert get_state_dictionary(coll_correct, state="canceled") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_get_state_dictionary_empty_and_uncorrect(coll_uncorrect: Any) -> None:
    assert get_state_dictionary(coll_uncorrect) is None


def test_get_list_sorted_date_correct(coll_correct: list) -> None:
    assert get_list_sorted_date(coll_correct, sort_reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_get_list_sorted_date_empty_and_uncorrect(coll_uncorrect: Any) -> None:
    assert get_list_sorted_date(coll_uncorrect) is None
