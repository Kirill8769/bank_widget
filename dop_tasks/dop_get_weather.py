import json
import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API")


def get_weather(city: str) -> dict | str:
    """
    Получает информацию о погоде для указанного города,
    извлекает из ответа необходимые данные (температура, давление, влажность и т.д.),
    возвращает полученную информацию о погоде

    :param city: Название города.
    :return: Словарь с информацией о погоде или сообщение об ошибке.
    """
    try:
        params = {"q": city, "appid": api_key}
        url = "http://api.openweathermap.org/geo/1.0/direct"
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            city_info = json.loads(response.text)[0]
        else:
            return f"Connection Error. Status code: {response.status_code}"
        params = {"lat": city_info["lat"], "lon": city_info["lon"], "appid": api_key, "units": "metric"}
        url = "https://api.openweathermap.org/data/2.5/weather"
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            data = json.loads(response.text)
            utc_time = datetime.utcfromtimestamp(data["dt"])
            timezone = timedelta(seconds=data["timezone"])
            city_time = (utc_time + timezone).strftime("%d.%m.%Y %H:%M:%S")
            result = {
                "Погода в городе": city,
                "Температура": f"{data['main']['temp']} ℃",
                "Ощущается как": f"{data['main']['feels_like']} ℃",
                "Скорость ветра": f"{data['wind']['speed']} м/с",
                "Давление": data["main"]["pressure"],
                "Влажность": f"{data['main']['humidity']}%",
                "Текущее время": city_time,
            }
            return result
        else:
            return f"Connection Error. Status code: {response.status_code}"
    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"


weather_info = get_weather("Moscow")


if isinstance(weather_info, dict):
    for key, value in weather_info.items():
        print(f"{key}: {value}")
else:
    print(weather_info)
