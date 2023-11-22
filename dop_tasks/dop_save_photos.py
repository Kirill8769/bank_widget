import logging
import os

import requests

log_path = os.path.join(os.getcwd(), "dop_tasks", "log_photos.log")


logging.basicConfig(
    filename=log_path, encoding="UTF-8", level=logging.INFO, format="%(levelname)s:%(name)s:%(message)s"
)


def get_images(album_id: int, limit: int = 100) -> None:
    logging.info("Starting app...")
    params = {"albumId": album_id}
    response = requests.get("https://jsonplaceholder.typicode.com/photos", params=params)
    if response.status_code == 200:
        logging.info(f"Downloading album {album_id} images...")
        total_images = 0
        if not os.path.isdir("photos"):
            os.mkdir("photos")
        for info in response.json()[:limit]:
            response_jpg = requests.get(info["url"])
            if response_jpg.status_code == 200:
                filename = f"{info['albumId']}-{info['id']}.jpg"
                filepath = os.path.join(os.getcwd(), "photos", filename)
                with open(filepath, "wb") as file_jpg:
                    file_jpg.write(response_jpg.content)
                    total_images += 1
                    logging.info(f"Saving image {info['id']} to {os.path.join('photos', filename)}")
        logging.info(f"Finished downloading images. Total images downloaded: {total_images}")


get_images(album_id=1, limit=7)
