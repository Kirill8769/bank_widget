from typing import Any

import requests

from src.decorators import retry
from src.my_logger import logger


@retry(3)
def get_actual_currency(currency: str) -> Any:
    """
    Получает актуальный курс валюты из внешнего источника.

    :param currency: Код валюты (например, "RUB").
    :return: Актуальный курс валюты.
    """
    try:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        if response.status_code == 200:
            currency_info = response.json()
            return currency_info["Valute"][currency]["Value"]
        return []

    except KeyError:
        logger.warning('Функция работает только с "RUB", "USD" и "EUR"')
        return 'KeyError: Функция работает только с "RUB", "USD" и "EUR"'

    except Exception as ex:
        error = f"{ex.__class__.__name__}: {ex}"
        logger.error(error)
        return error
