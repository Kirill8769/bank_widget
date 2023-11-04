from test_data import test_operation_info


def get_state_dictionary(state_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает на вход список словарей
    и значение для ключа state со значением по умолчанию EXECUTED
    и возвращает новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение

    :param state_list: Список словарей
    :param state: Параметр фильтрации со значением по умолчанию EXECUTED
    :return: Новый список, содержащий только те словари,
    у которых ключ state содержит переданное в функцию значение
    """
    result = [state_dict for state_dict in state_list if state_dict["state"] == state.upper()]
    return result


def get_list_sorted_date(state_list: list[dict], sort_reverse: bool = True) -> list[dict]:
    """
    Функция принимает на вход список словарей и возвращает новый список,
    в котором исходные словари отсортированы по убыванию даты

    :param state_list: Список словарей
    :param sort_reverse: Параметр реверса сортировки, по умолчанию True
    :return: Отсотированный список
    """
    result = sorted(state_list, key=lambda x: x["date"], reverse=sort_reverse)
    return result


print(get_state_dictionary(test_operation_info, state="CANceLED"))
print(get_list_sorted_date(test_operation_info))
