import requests
import argparse
import os
from urllib.parse import urlparse
from configure_keys import load_keys
from images_saver import save_img
from file_extension import extension_returner


def check_url(json):
    try:
        img_url = json['hdurl']
        save_img(img_url,
                 os.path.splitext(os.path.split((urlparse(img_url)).path)[1])[0],
                 extension_returner(img_url), "images")
    except KeyError:
        try:
            img_url = json['url']
            youtube_check = urlparse(img_url)
            if youtube_check.netloc == 'www.youtube.com':
                pass
            else:
                save_img(img_url,
                         os.path.splitext(os.path.split((urlparse(img_url)).path)[1])[0],
                         extension_returner(img_url), "images")
        except KeyError:
            pass


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт загружает и сохраняет Последние APOD-фото от NASA'
    )
    parser.add_argument("-da", default=None,
                        help="Загрузит APOD-фото от NASA за указаный день в формате 2024-06-15")
    args = parser.parse_args()
    return args


def request_nasa(token, date):
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
    args = args_parser()
    image_response = request_nasa(load_keys("NASE_KEY"), date=args.da)
    if isinstance(image_response, list):
        for image in image_response:
            check_url(image)
    else:
        check_url(image_response)


if __name__ == '__main__':
    main()
