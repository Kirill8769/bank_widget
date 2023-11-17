import os
import time
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


def retry(repeats: int = 3):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            for i in range(repeats):
                print(i)
                try:
                    print(11)
                    result = func(*args, **kwargs)
                    print(111)
                    return result
                except ConnectionError:
                    print(22)
                    time.sleep(3)
                print(33)
            return ConnectionError("Попытки подключиться к сайту не увенчались успехом")
        return inner
    return wrapper
