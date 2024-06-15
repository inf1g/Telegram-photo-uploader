import requests
import argparse
import os
from urllib.parse import urlparse
from configure_keys import load_keys
from images_saver import saving_img
from file_extension import extension_returner


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт загружает и сохраняет Последние APOD-фото от NASA'
    )
    parser.add_argument("-d", "--date", help="Загрузит APOD-фото от NASA за указаный день в формате 2024-06-15")
    args = parser.parse_args()
    nasa_token = load_keys("NASE_KEY")
    path = "images_nasa_APOD\\"
    if not args.date:
        path = "images_nasa_APOD\\"
        for image in nasa_planetary_requests(nasa_token):
            try:
                print(os.path.splitext(os.path.split((urlparse(image["hdurl"])).path)[1])[0])
                print(os.path.split((urlparse(image["hdurl"])).path)[1])
                saving_img(image["hdurl"], os.path.splitext(os.path.split((urlparse(image["hdurl"])).path)[1])[0],
                              extension_returner(image["hdurl"]), path)
            except KeyError:
                saving_img(image["url"], os.path.splitext(os.path.split((urlparse(image["url"])).path)[1])[0],
                              extension_returner(image["url"]), path)
    else:
        try:
            image = nasa_planetary_requests(nasa_token, date=args.date)['hdurl']
            saving_img(image, os.path.splitext(os.path.split((urlparse(image)).path)[1])[0],
                       extension_returner(image), path)
        except KeyError:
            image = nasa_planetary_requests(nasa_token, date=args.date)['hdurl']
            saving_img(image, os.path.splitext(os.path.split((urlparse(image)).path)[1])[0],
                              extension_returner(image), path)


def nasa_planetary_requests(token, date=None):
    url = "https://api.nasa.gov/planetary/apod"
    if not date:
        payload = {
            "api_key": token,
            "count": "30"
        }
    else:
        payload = {
            "api_key": token,
            "date": {date}
        }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def main():
    args_parser()


if __name__ == '__main__':
    main()
