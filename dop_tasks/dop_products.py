def get_sorted_products(list_products: list[dict],
                        category: str | None = None) -> list[dict]:
    """
    Функция принимает на вход список словарей с товарами,
    сортирует их по убыванию цены и возвращает новый список словарей

    :param list_products: Список словарей с товарами
    :param category: Категория товара, используется для сортировки, необязательный
    :return: Отсортированный список словарей с товарами
    """
    if category:
        list_products = [product for product in list_products if product['category'] == category.lower()]
    result = sorted(list_products, key=lambda x: x['price'], reverse=True)
    return result


list_products = [
    {'name': 'apple', 'price': 25, 'category': 'fruit', 'quantity': 11},
    {'name': 'banana', 'price': 20, 'category': 'fruit', 'quantity': 17},
    {'name': 'potato', 'price': 8, 'category': 'vegetable', 'quantity': 85},
    {'name': 'carrot', 'price': 12, 'category': 'vegetable', 'quantity': 30},
]

print(get_sorted_products(list_products, category='Fruit'))
