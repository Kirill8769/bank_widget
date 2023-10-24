import masks


def get_hidden_info(info: str) -> str:
    name_info = ' '.join(info.split()[0:-1])
    num_info = info.split()[-1]
    hidden_num_info = masks.get_mask_card(num_info) if len(num_info) == 16 else masks.get_mask_invoice(num_info)
    return name_info + ' ' + hidden_num_info


print(get_hidden_info('Visa Classic 6831982476737658'))
print(get_hidden_info('Счет 64686473678894779589'))
print(get_hidden_info('Maestro 1596837868705199'))
print(get_hidden_info('Visa Platinum 8990922113665229'))