from widget import get_hidden_info
from test_info import test_widget_info


def main():
    for info in test_widget_info:
        print(get_hidden_info(info=info))


if __name__ == '__main__':
    main()