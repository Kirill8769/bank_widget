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


def retry(repeats: int) -> Callable:
    """
    Декоратор, повторяющий выполнение функции в случае возникновения ошибки подключения.

    :param repeats: Количество попыток выполнения функции.
    :return: Декорированная функция.
    """

    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: tuple, **kwargs: dict) -> Any:
            for _ in range(repeats):
                result = func(*args, **kwargs)
                if isinstance(result, str) and "ConnectionError" in result:
                    time.sleep(1)
                    continue
                return result
            return ConnectionError("Попытки подключиться к сайту не увенчались успехом")

        return inner

    return wrapper
