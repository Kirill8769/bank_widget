from datetime import datetime


def get_clean_date(dirty_date: str) -> str:
    """
    Преобразует строку даты в формате ISO в формат "DD.MM.YYYY".

    :param: dirty_date: Входная строка с датой в формате ISO.
    :type dirty_date: str
    :return: Отформатированная строка даты в формате "DD.MM.YYYY".
    :rtype: str
    """
    try:
        format_date = datetime.fromisoformat(dirty_date)
        clean_date = datetime.strftime(format_date, '%d.%m.%Y')
        return clean_date
    except Exception as ex:
        print(f'Неверный формат даты: {ex}')
