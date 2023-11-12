import os

from src.decorators import log


@log(filename="mylog.log")
def my_function(x, y):
    return x + y


def test_log_decorator_with_filename():
    assert my_function(1, 2) == 3
    assert my_function("str", 2) is None

    file_path = os.path.join("..", "mylog.log")
    assert os.path.isfile(file_path) is True

    with open(file_path, "r", encoding="UTF-8") as file:
        log_content = file.read()
        assert f"{my_function.__name__} ok" in log_content
        assert 'can only concatenate str (not "int") to str' in log_content
        assert "Input: ('str', 2), {}" in log_content


@log()
def my_function_no_filename(x, y):
    return x + y


def test_log_decorator_without_filename():
    assert my_function(1, 2) == 3
    assert my_function("str", 2) is None
