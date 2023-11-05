from datetime import datetime

from src.masks import get_mask_card, get_mask_invoice


def get_hidden_info(info: str) -> str:
    """
    Скрывает конфиденциальную информацию в строке 'info'
    и возвращает обработанную строку.

    :param info: Строка, содержащая информацию о карте или счёте.
    :return: Обработанная строка с скрытой конфиденциальной информацией.
    """
    try:
        name_info = " ".join(info.split()[0:-1])
        num_info = info.split()[-1]
        hidden_num_info = get_mask_card(num_info) if len(num_info) == 16 else get_mask_invoice(num_info)
        return name_info + " " + hidden_num_info
    except Exception as ex:
        print(f"Error get_hidden_info: {ex}")
        return ""


def get_clean_date(dirty_date: str) -> str | None:
    """
    Преобразует строку даты в формате ISO в формат "DD.MM.YYYY".

    :param dirty_date: dirty_date: Входная строка с датой в формате ISO.
    :return: Отформатированная строка даты в формате "DD.MM.YYYY".
    """
    try:
        format_date = datetime.fromisoformat(dirty_date)
        clean_date = datetime.strftime(format_date, "%d.%m.%Y")
        return clean_date
    except Exception as ex:
        print(f"Неверный формат даты: {ex}")
        return None
