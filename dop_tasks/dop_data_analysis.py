import json
import os
from datetime import datetime


def get_analysis_data(user_filepath: str) -> str:
    """
    Функция получает путь к json файлу с продажами, анализирует,
    и выводит суммарные продажи по дням недели

    :param user_filepath: Путь к json файлу
    :return: Результат в удобочитаемом виде
    """
    try:
        with open(user_filepath, "r") as file:
            data = json.load(file)
            week_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
            result = {day: 0 for day in week_days}
            for sale in data["sales"]:
                date_object = datetime.strptime(sale["date"], "%Y-%m-%d")
                week_day = week_days[date_object.weekday()]
                result[week_day] += sale["price"] * sale["quantity"]

            message = "\n".join([f"{day}: {sales_sum:.2f}" for day, sales_sum in result.items()])
            return f"Суммы продаж по дням недели:\n{message}"
    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"


path_project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
filepath = os.path.join(path_project, "data", "data.json")


print(get_analysis_data(filepath))
