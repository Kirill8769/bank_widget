import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Декоратор для логирования результатов выполнения функции с записью в файл или выводом в консоль.

    :param filename: Имя файла для записи логов.
    :return: Декорированная функция.
    """

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


def retry(repeat: int):
    def wrapper(func):
        pass
        @wraps(func)
        def inner(*args, **kwargs):
            pass
        return inner
    return wrapper
