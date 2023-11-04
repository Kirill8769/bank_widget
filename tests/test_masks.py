import pytest

from src.masks import get_mask_card, get_mask_invoice


@pytest.fixture
def coll():
    return ['One', True, 3, [1, 'hello', [0]], 'hi', {}, '', [], False]


@pytest.mark.parametrize('info, expected', [('1596837868705199', '1596 83** **** 5199'),
                                            ('8990922113665229', '8990 92** **** 5229')])
def test_get_mask_card_correct(info, expected):
    assert get_mask_card(info) == expected


def test_get_mask_card_empty_and_uncorrect(coll):
    assert get_mask_card(coll) == None


@pytest.mark.parametrize('info, expected', [('73654108430135874305', '**4305'),
                                            ('35383033474447895560', '**5560')])
def test_get_mask_invoice_correct(info, expected):
    assert get_mask_invoice(info) == expected


def test_get_mask_invoice_empty_and_uncorrect(coll):
    assert get_mask_invoice(coll) == None