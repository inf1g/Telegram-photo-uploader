import requests
import os
from dotenv import load_dotenv


def configure_keys(token):
    load_dotenv()
    key = os.getenv(token)
    return key


def fetch_spacex_launch(url, filename, path="images\\"):
    os.makedirs(f"{path}", exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(f"{path}{filename}.jpeg", 'wb') as file:
        file.write(response.content)


def api_get_request():
    response = requests.get("https://api.spacexdata.com/v5/launches/6243ad8baf52800c6e919252")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    configure_keys("NASE_KEY")
    path = "images\\"
    for image_name, image_url in enumerate(api_get_request()):
        fetch_spacex_launch(image_url, image_name, path)


if __name__ == '__main__':
    main()