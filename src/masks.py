import re

from src.my_logger import logger


def get_mask_card(input_card: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя только первые 6 и последние 4 цифры.

    :param card: Номер кредитной карты для маскирования (целое число).
    :return: Маскированный номер кредитной карты.
    """
    mask_card = ""
    try:
        if not isinstance(input_card, str):
            raise TypeError("Неверный формат карты, принимается только str")
        if not input_card.isdigit():
            raise ValueError("В стоке должны быть только цифры")
        pattern = re.compile(r"\d{16}")
        card_verification = pattern.search(input_card)
        if card_verification:
            card = card_verification[0]
            mask_card = card[0:4] + " " + card[4:6] + "** **** " + card[-4::]
            logger.info("Номер карты замаскирован")
    except TypeError as type_ex:
        logger.error(f"{type_ex.__class__.__name__}: {type_ex}")
    except ValueError as val_ex:
        logger.error(f"{val_ex.__class__.__name__}: {val_ex}")
    except Exception as ex:
        logger.debug(f"{ex.__class__.__name__}: {ex}")
    finally:
        return mask_card


def get_mask_invoice(inpit_invoice: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры.

    :param invoice: Номер счета для маскирования (целое число).
    :return: Маскированный номер счета.
    """
    mask_invoice = ""
    try:
        if not isinstance(inpit_invoice, str):
            raise TypeError("Неверный формат счета, принимается только str")
        if not inpit_invoice.isdigit():
            raise ValueError("В стоке должны быть только цифры")
        pattern = re.compile(r"\d{20}")
        invoice_verification = pattern.search(inpit_invoice)
        if invoice_verification:
            invoice = invoice_verification[0]
            mask_invoice = "**" + invoice[-4:]
            logger.info("Номер счета замаскирован")
    except TypeError as type_ex:
        logger.error(f"{type_ex.__class__.__name__}: {type_ex}")
    except ValueError as val_ex:
        logger.error(f"{val_ex.__class__.__name__}: {val_ex}")
    except Exception as ex:
        logger.debug(f"{ex.__class__.__name__}: {ex}")
    finally:
        return mask_invoice
