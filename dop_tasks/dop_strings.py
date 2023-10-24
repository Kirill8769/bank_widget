from src.test_data import test_string


def get_filter_strings(string_list: list[list[str]]) -> list:
    """
    Функция фильтрует список строк и возвращает только те строки,
    в которых первая и последняя буквы совпадают.

    :param string_list (list[list[str]]): Список списков строк для фильтрации.
    :return (list): Список строк, в которых первая и последняя буквы совпадают.
    """  
    result_list = []

    for words in string_list:
        result = []
        for word in words:
            if word and isinstance(word, str) and word[0] == word[-1]:
                result.append(word)
        else:
            result_list.append(result)
    return result_list


print(get_filter_strings(test_string))