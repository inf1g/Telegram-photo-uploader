import datetime
import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv
import images_saver
import subprocess
import sys





def configure_keys(token):
    load_dotenv()
    key = os.getenv(token)
    return key


def spacex_request():
    response = requests.get("https://api.spacexdata.com/v5/launches/6243ad8baf52800c6e919252")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def nasa_planetary_requests(token):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": token,
        "count": "30"
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def nasa_epic_requests(token):
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": token
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def file_extension(url):
    return os.path.splitext(urlparse(url).path)[1]


def saving_images(url, filename, image_format="jpeg", path="images\\", payload=()):
    os.makedirs(f"{path}", exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(f"{path}{filename}.{image_format}", 'wb') as file:
        file.write(response.content)


def main():
    nasa_token = configure_keys("NASE_KEY")
    path = "images_nasa\\"
    for image_name, image_url in enumerate(spacex_request()):
        saving_images(image_url, image_name, file_extension(image_url))
    for image in nasa_planetary_requests(nasa_token):
        try:
            saving_images(image["hdurl"], os.path.splitext(os.path.split((urlparse(image["hdurl"])).path)[1])[0],
                          file_extension(image["hdurl"]), path)
        except KeyError:
            saving_images(image["url"], os.path.splitext(os.path.split((urlparse(image["url"])).path)[1])[0],
                          file_extension(image["url"]), path)
    payload = {"api_key": nasa_token}
    for image in nasa_epic_requests(nasa_token):
        image_name = image["image"]
        date = datetime.date.fromisoformat(image["date"].split(" ")[0])
        month = image["date"].split("-")[1]
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{month}/{date.day}/png/{image_name}.png"
        saving_images(url, image_name, "png", "images_nasa_EPIC\\", payload)


if __name__ == '__main__':
    main()


def main():
    args = ["-u https://images.wallpaperscraft.ru/image/single/margaritka_lepestki_tsvetok_1252445_300x168.jpg", "-f name", "-if jpeg", "-p image-test\\"]

    subprocess.call([sys.executable, "images_saver.py"] + args)



if __name__ == "__main__":
    main()

