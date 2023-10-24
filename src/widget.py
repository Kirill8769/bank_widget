from src.masks import get_mask_card, get_mask_invoice


def get_hidden_info(info: str) -> str:
    """
    Скрывает конфиденциальную информацию в строке 'info' и возвращает обработанную строку.

    :param info: Строка, содержащая информацию о карте или счёте.
    :type info: str
    :return: Обработанная строка с скрытой конфиденциальной информацией.
    :rtype: str
    """
    name_info = " ".join(info.split()[0:-1])
    num_info = info.split()[-1]
    hidden_num_info = get_mask_card(num_info) if len(num_info) == 16 else get_mask_invoice(num_info)
    return name_info + " " + hidden_num_info
