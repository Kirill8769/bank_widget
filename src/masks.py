def get_mask_card(card: int) -> str:
    """
    Маскирует номер кредитной карты, оставляя только первые и последние 4 цифры.

    :param card: Номер кредитной карты для маскирования (целое число).
    :type card: int
    :return: Маскированный номер кредитной карты.
    :rtype: str
    """
    str_card = str(card)
    mask_card = str_card[0:4] + " " + str_card[4:6] + "** **** " + str_card[-4::]
    return mask_card


def get_mask_invoice(invoice: int) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры.

    :param invoice: Номер счета для маскирования (целое число).
    :type invoice: int
    :return: Маскированный номер счета.
    :rtype: str
    """
    str_invoice = str(invoice)
    mask_invoice = "**" + str_invoice[-4::]
    return mask_invoice


print(get_mask_card(7000792289606361))
print(get_mask_invoice(73654108430135874305))
