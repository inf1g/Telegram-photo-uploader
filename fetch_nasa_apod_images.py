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
    if not args.date:
        for image in nasa_requests(load_keys("NASE_KEY")):
            try:
                saving_img(image["hdurl"], os.path.splitext(os.path.split((urlparse(image["hdurl"])).path)[1])[0],
                           extension_returner(image["hdurl"]), "images\\")
            except KeyError:
                if urlparse(image["url"]).netloc == "www.youtube.com":
                    continue
                else:
                    saving_img(image["url"], os.path.splitext(os.path.split((urlparse(image["url"])).path)[1])[0],
                               extension_returner(image["url"]), "images\\")
    else:
        try:
            image = nasa_requests(load_keys("NASE_KEY"), date=args.date)['hdurl']
            saving_img(image, os.path.splitext(os.path.split((urlparse(image)).path)[1])[0],
                       extension_returner(image), "images\\")
        except KeyError:
            image = nasa_requests(load_keys("NASE_KEY"), date=args.date)['url']
            saving_img(image, os.path.splitext(os.path.split((urlparse(image)).path)[1])[0],
                       extension_returner(image), "images\\")


def nasa_requests(token, date=None):
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
