from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency: str) -> Generator:
    """
    Фильтрует список транзакций на основе указанной валюты.

    :param transactions_list: Список транзакций, представленных в виде словарей.
    :param currency: Валюта, по которой необходимо выполнить фильтрацию.

    :yield: Генератор возвращает транзакции, у которых валюта совпадает с указанной.
    """
    for transaction in transactions_list:
        if transaction["operationAmount"]["currency"]["name"] == currency:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]) -> Generator:
    """
    Извлекает описания транзакций из списка.

    :param transactions_list: Список транзакций, представленных в виде словарей.

    :yield: Генератор возвращает описания транзакций в виде строк.
    """
    for transaction in transactions_list:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Generator:
    """
    Генерирует номера карт в заданном диапазоне.

    :param start: Начальное значение для генерации номеров карт.
    :param stop: Конечное значение для генерации номеров карт.

    :yield: Генератор возвращает сгенерированные номера карт в виде строк.
    """
    for i in range(start, stop + 1):
        number = str(i).rjust(16, "0")
        format_number = number[0:4] + " " + number[4:8] + " " + number[8:12] + " " + number[12:16]
        yield format_number
