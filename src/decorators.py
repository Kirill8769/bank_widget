import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Пока никакого описания тут нет
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple, **kwargs: dict) -> Any:
            date_info = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
            try:
                result = func(*args, **kwargs)
                print(bool(result))
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
    raise TypeError("ERROR")
    return x + y


print(my_function(1, 2))
