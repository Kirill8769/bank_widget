import pytest

from src.processing import get_list_sorted_date, get_state_dictionary


@pytest.fixture
def data_correct():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def data_incorrect():
    return ["One", True, 3, [1, "hello", [0]], "hi", {}, "", [], False]


def test_get_state_dictionary_correct(data_correct):
    assert get_state_dictionary(data_correct, state="canceled") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_get_state_dictionary_empty_and_incorrect(data_incorrect):
    assert get_state_dictionary(data_incorrect) is None


def test_get_list_sorted_date_correct(data_correct):
    assert get_list_sorted_date(data_correct, sort_reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_get_list_sorted_date_empty_and_incorrect(data_incorrect):
    assert get_list_sorted_date(data_incorrect) is None
