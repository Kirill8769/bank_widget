import requests
import json


def get_weather(city: str):
    params_coordinates = {"q": "Tver", "appid": "f2e75f632ec10b226436cf8c9201f912"}
    url = "http://api.openweathermap.org/geo/1.0/direct"
    response = requests.get(url=url, params=params_coordinates)
    ss = json.loads(response.text)[0]

    print(ss["lat"], ss["lon"])

    s_lat = ss["lat"]
    s_lon = ss["lon"]


    params_weather = {"lat": s_lat, "lon": s_lon, "appid": "f2e75f632ec10b226436cf8c9201f912", "units": "metric", "lang": "ru"}
    url_2 = "https://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url=url_2, params=params_weather)
    ss12 = json.loads(response.text)

    print(ss12)

# http://api.openweathermap.org/geo/1.0/reverse?lat={lat}&lon={lon}&limit={limit}&appid={API key}

get_weather("dd")


# f2e75f632ec10b226436cf8c9201f912


# info city https://openweathermap.org/api/geocoding-api

# info weather https://openweathermap.org/current