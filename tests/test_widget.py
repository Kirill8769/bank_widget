import pytest

from src.widget import get_hidden_info


@pytest.mark.parametrize('info, expected', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                            ('Счет 35383033474447895560', 'Счет **5560'),
                                            ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229')])
def test_get_hidden_info_(info, expected):
    assert get_hidden_info(info) == expected


def test_get_hidden_info_type():
    with pytest.raises(TypeError):
        get_hidden_info(100)