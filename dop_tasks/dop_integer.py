def get_max_integer(int_list: list[int]) -> int:
    """
    Находит произведение двух наибольших целых чисел в списке.
    Если в списке менее двух элементов, возвращается 0.

    :param int_list (list[int]): Список целых чисел
    :return (int): Произведение двух наибольших целых чисел в списке.
    """
    if len(int_list) < 2:
        return 0
    
    result = 1
    abs_int_list = sorted([abs(number) for number in int_list])
    for number in abs_int_list[-2:]:
        result *= number
    return result


print(get_max_integer([2, 3, 5, 7, 11]))
print(get_max_integer([-5, -7, -9, -13]))
print(get_max_integer([1, 2]))
print(get_max_integer([4]))
