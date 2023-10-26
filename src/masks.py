def get_mask_card(card: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя только первые и последние 4 цифры.

    :param card: Номер кредитной карты для маскирования (целое число).
    :return: Маскированный номер кредитной карты.
    """
    mask_card = card[0:4] + " " + card[4:6] + "** **** " + card[-4::]
    return mask_card


def get_mask_invoice(invoice: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры.

    :param invoice: Номер счета для маскирования (целое число).
    :return: Маскированный номер счета.
    """
    mask_invoice = "**" + invoice[-4::]
    return mask_invoice
