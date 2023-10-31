def get_orders_info(list_orders: list[dict]) -> dict:
    """
    Функция принимает список заказов, сортирует их по месяцам,
    считает количество и среднюю стоимость заказов за месяц

    :param list_orders: Список словарей с онлайн заказами
    :return: Новый список, с количеством заказов и их средней суммой разбитые по месяцам
    """
    result: dict = {}
    for order in list_orders:
        buy_date = order["date"][:-3]
        if not result.get(buy_date):
            result[buy_date] = {"average_order_value": 0, "order_count": 0}
        for item in order["items"]:
            result[buy_date]["order_count"] += 1
            average_order_value = item["quantity"] * item["price"]
            result[buy_date]["average_order_value"] += average_order_value

    for key, value in result.items():
        result[key]["average_order_value"] = value["average_order_value"] / value["order_count"]
    return result


list_products = [
    {
        "id": 1,
        "date": "2023-10-21",
        "items": [{"name": "potato", "price": 8, "quantity": 2}, {"name": "apple", "price": 25, "quantity": 2}],
    },
    {
        "id": 2,
        "date": "2023-10-31",
        "items": [{"name": "carrot", "price": 12, "quantity": 1}, {"name": "banana", "price": 20, "quantity": 4}],
    },
    {
        "id": 4,
        "date": "2023-08-21",
        "items": [{"name": "potato", "price": 8, "quantity": 5}, {"name": "apple", "price": 25, "quantity": 3}],
    },
    {
        "id": 7,
        "date": "2022-10-22",
        "items": [{"name": "carrot", "price": 12, "quantity": 6}, {"name": "banana", "price": 20, "quantity": 7}],
    },
]

print(get_orders_info(list_products))
