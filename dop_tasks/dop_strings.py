def get_filter_strings(string_list: list[str]) -> list[str]:
    """
    Функция фильтрует список строк и возвращает только те строки,
    в которых первая и последняя буквы совпадают.

    :param string_list: Список строк для фильтрации.
    :return (list): Список строк, в которых первая и последняя буквы совпадают.
    """
    result_list = []
    for word in string_list:
        if word and isinstance(word, str) and word[0] == word[-1]:
            result_list.append(word)
    return result_list


test_string: list[list[str]] = [
    ["pop"],
    ["hello", "world", "apple", "pear", "banana", "pop"],
    ["", "madam", "racecar", "noon", "level", ""],
    [],
]

for string in test_string:
    print(get_filter_strings(string))
