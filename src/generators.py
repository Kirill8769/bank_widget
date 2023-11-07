def filter_by_currency(transactions_list: list[dict], currency: str):
    for transaction in transactions_list:
        if transaction['operationAmount']['currency']['name'] == currency:
            yield transaction


def transaction_descriptions(transactions_list: list[dict]):
    for transaction in transactions_list:
        yield transaction['description']


def card_number_generator(start: int, stop: int):
    for i in range(start, stop + 1):
        number = str(i).rjust(16, '0')
        format_number = number[0:4] + ' ' + number[4:8] + ' ' + number[8:12] + ' ' + number[12:16]
        yield format_number
