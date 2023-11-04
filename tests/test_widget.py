import pytest

from src.widget import get_hidden_info, get_clean_date


@pytest.fixture
def coll():
    return ['One', True, 3, [1, 'hello', [0]], 'hi', {}, '', [], False]


@pytest.mark.parametrize('info, expected', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                            ('Счет 35383033474447895560', 'Счет **5560'),
                                            ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229')])
def test_get_hidden_info_correct(info, expected):
    assert get_hidden_info(info) == expected


def test_get_hidden_info_empty_and_uncorrect(coll):
    assert get_hidden_info(coll) == None


@pytest.mark.parametrize('test_date, expected', [
    ('2018-07-11T02:26:18.671407', '11.07.2018'),
    ("2023-11-04", '04.11.2023')
    ])
def test_get_clean_date_correct_date(test_date, expected):
    assert get_clean_date(test_date) == expected


def test_get_clean_date_empty_and_uncorrect(coll):
    assert get_clean_date(coll) == None