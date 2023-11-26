from collections import defaultdict

from src.my_logger import logger


def get_filtered_transactions_by_search_string(transactions: list[dict], search: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и строку поиска и возвращает
    список словарей, у которых в описании есть данная строка.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search: Строка для поиска.
    :return: Список словарей, у которых в описании есть искомая строка.
    """
    output_list = []
    try:
        if not isinstance(transactions, list) or not isinstance(transactions[0], dict):
            raise TypeError("Передан неверный формат списка транзакций")
        if not isinstance(search, str):
            raise TypeError("Передан неверный поисковый запрос")
        output_list = [
            transaction
            for transaction in transactions
            if transaction.get("description") and search.lower() in transaction["description"].lower()
        ]
    except TypeError as type_ex:
        logger.error(f"{type_ex.__class__.__name__}: {type_ex}")
    except Exception as ex:
        logger.debug(f"{ex.__class__.__name__}: {ex}")
    finally:
        return output_list


def get_filtered_transactions_by_category(
    transactions: list[dict], category: dict[str, int] = defaultdict(int)
) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и словарь категорий операций и возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.

    :param transactions: Список словарей с данными о банковских операциях.
    :param search: Словарь категорий.
    :return: Словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    output_dict = {}
    try:
        if not isinstance(transactions, list) or not isinstance(transactions[0], dict):
            raise TypeError("Передан неверный формат списка транзакций")
        if (
            not isinstance(category, dict)
            or category
            and not all(isinstance(digit, int) for digit in category.values())
        ):
            raise TypeError("Передан неверный формат категорий")
        for transaction in transactions:
            if transaction.get("description"):
                try:
                    category[transaction["description"]] += 1
                except KeyError:
                    continue
        output_dict = dict(category)
    except TypeError as type_ex:
        logger.error(f"{type_ex.__class__.__name__}: {type_ex}")
    except Exception as ex:
        logger.debug(f"{ex.__class__.__name__}: {ex}")
    finally:
        return output_dict
