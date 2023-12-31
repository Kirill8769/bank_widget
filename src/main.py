from test_data import test_widget_info
from widget import get_hidden_info


def main() -> None:
    """
    Главная функция, которая обрабатывает
    информацию в `test_widget_info` и выводит скрытую информацию.

    :return: None
    """
    for info in test_widget_info:
        print(get_hidden_info(info=info))


if __name__ == "__main__":
    main()
