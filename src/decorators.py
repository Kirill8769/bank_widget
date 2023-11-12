import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Пока никакого описания тут нет
    """
    print(1)
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple, **kwargs: dict) -> Any:
            date_info = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                message = f"{date_info} {func.__name__} ok\n"
            except Exception as ex:
                result = None
                message = f"{date_info} {func.__name__} error: {ex}. Input: {args}, {kwargs}\n"
            if filename:
                file_path = os.path.join("..", filename)
                file_mode = "a" if os.path.isfile(file_path) else "w"
                with open(file_path, file_mode, encoding="UTF-8") as file:
                    file.write(message)
            else:
                print(message)
            return result

        return inner

    return wrapper


@log(filename="mylog.txt")
def my_function(x, y):
    # raise TypeError("ERROR")
    return x + y


print(my_function(1, 2))


def memoized(cache_count: int) -> Callable:
    """
    Пока никакого описания тут нет
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


@memoized(3)
def f(x):
    print("Calculating...")
    return x * 10


# print(f(1))
# # => Calculating...
# # 10
# print(f(1))
# # 10
# print(f(42))
# # => Calculating...
# # 420
# print(f(42))
# # 420
# print(f(1))
# # 10
print(f(1))
# => Calculating...
# 10
print(f(1))  # Будет «вспомнено»
# 10
print(f(2))
# => Calculating...
# 20
print(f(3))
# => Calculating...
# 30
print(f(4))  # Вытеснит запомненный результат для «1»
# => Calculating...
# 40
print(f(1))  # Будет перевычислено
# => Calculating...
# 10
