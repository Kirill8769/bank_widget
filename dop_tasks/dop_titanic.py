import json
import os

import pandas as pd

filepath = os.path.join("data", "titanic.csv")


def get_filtered_df(filepath: str) -> pd:
    """
    Функция фильтрует пассажиров, у которых цена билета больше 50 и возраст меньше 30 лет,
    затем функция сортирует отфильтрованный DataFrame по имени пассажира в алфавитном
    порядке и возвращает результат.

    :param filepath: Путь к обрабатываемому файлу.
    :return: Отфильтрованный и отсортированный результат.
    """
    df = pd.read_csv(filepath)
    filtered_df = df[(df["Fare"] > 50) & (df["Age"] < 30)]
    sorted_df = filtered_df.sort_values("Name")
    return sorted_df


# print(get_filtered_df(filepath))


def get_groupby_json(filepath: str) -> list:
    """
    Функция группирует пассажиров по классу и считает среднюю стоимость
    билета и количество пассажиров в каждом классе.

    :param filepath: Путь к обрабатываемому файлу.
    :return: Результат в виде словаря в формате JSON.
    """
    df = pd.read_csv(filepath)
    group_df = df.groupby("Pclass")
    total_passengers = group_df["Name"].count()
    avg_fare = group_df["Fare"].mean()
    result = {}
    for i, fare, passengers in zip(avg_fare.index, avg_fare, total_passengers):
        result[f"{i}st"] = {"average_ticket_price": round(fare, 2), "passenger_count": int(passengers)}
    return json.dumps(result)


# print(get_groupby_json(filepath))


