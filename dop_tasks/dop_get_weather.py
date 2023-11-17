import json
import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("WEATHER_API")

print(api_key)


def get_weather(city: str) -> str:
    try:
        params = {"q": city, "appid": api_key}
        url = "http://api.openweathermap.org/geo/1.0/direct"
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            city_info = json.loads(response.text)
        else:
            return f"Connection Error. Status code: {response.status_code}"

        print(city_info)

        print(city_info["lat"], city_info["lon"])

        city_lat = city_info["lat"]
        city_lon = city_info["lon"]

        params = {"lat": city_lat, "lon": city_lon, "appid": api_key, "units": "metric"}
        url = "https://api.openweathermap.org/data/2.5/weather"
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            weather_info = json.loads(response.text)
            return weather_info
        else:
            return f"Connection Error. Status code: {response.status_code}"
    except Exception as ex:
        return f"{ex.__class__.__name__}: {ex}"


print(get_weather("Moscow"))
