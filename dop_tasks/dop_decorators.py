from functools import wraps
from typing import Any, Callable


def memoized(cache_count: int) -> Callable:
    """
    Декоратор для кэширования результатов функции с ограниченным количеством элементов в кэше.

    :param cache_count: Максимальное количество элементов в кэше.
    :return: Декорированная функция.
    """
    cache: dict[tuple, Any] = {}

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple) -> Any:
            if args in cache:
                return cache[args]
            else:
                if len(cache) >= cache_count:
                    for key in cache.keys():
                        del cache[key]
                        break
                result = func(*args)
                cache[args] = result
                return result

        return inner

    return wrapper
