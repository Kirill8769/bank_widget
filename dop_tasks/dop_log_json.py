import json
import logging
import os

import requests

filepath = os.path.join(os.getcwd(), "dop_tasks", "log.log")


logging.basicConfig(
    filename=filepath,
    encoding="UTF-8",
    level=logging.INFO,
    format="%(levelname)s:%(name)s:%(message)s: %(asctime)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def get_users_list() -> list:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        logging.info("Request time")
        users_list: list = json.loads(response.text)
        print(type(users_list))
        return users_list
    return []


print(get_users_list())
