from src.my_logger import logger


def get_mask_card(card: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя только первые 6 и последние 4 цифры.

    :param card: Номер кредитной карты для маскирования (целое число).
    :return: Маскированный номер кредитной карты.
    """
    try:
        mask_card = card[0:4] + " " + card[4:6] + "** **** " + card[-4::]
        logger.info("Номер карты замаскирован")
        return mask_card
    except Exception as ex:
        logger.error(ex)
        return ""


def get_mask_invoice(invoice: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры.

    :param invoice: Номер счета для маскирования (целое число).
    :return: Маскированный номер счета.
    """
    try:
        mask_invoice = "**" + invoice[-4::]
        logger.info("Номер счета замаскирован")
        return mask_invoice
    except Exception as ex:
        logger.error(ex)
        return ""
