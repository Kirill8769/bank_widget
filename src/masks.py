def get_mask_card(card: str) -> str:
    """
    Маскирует номер кредитной карты, оставляя только первые и последние 4 цифры.

    :param card: Номер кредитной карты для маскирования (целое число).
    :return: Маскированный номер кредитной карты.
    """
    try:
        mask_card = card[0:4] + " " + card[4:6] + "** **** " + card[-4::]
        return mask_card
    except Exception as ex:
        print(f"Error get_mask_card: {ex}")
        return ""


def get_mask_invoice(invoice: str) -> str:
    """
    Маскирует номер счета, оставляя только последние 4 цифры.

    :param invoice: Номер счета для маскирования (целое число).
    :return: Маскированный номер счета.
    """
    try:
        mask_invoice = "**" + invoice[-4::]
        return mask_invoice
    except Exception as ex:
        print(f"Error get_mask_invoice: {ex}")
        return ""
