import requests
import argparse
import os
from urllib.parse import urlparse
from configure_keys import load_keys
from images_saver import save_img
from file_extension import extension_returner


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт загружает и сохраняет Последние APOD-фото от NASA'
    )
    parser.add_argument("-da", default=None,
                        help="Загрузит APOD-фото от NASA за указаный день в формате 2024-06-15")
    args = parser.parse_args()
    image_response = request_nasa(load_keys("NASE_KEY"), date=args.da)
    if isinstance(image_response, list):
        for image in image_response:
            try:
                save_img(image['hdurl'], os.path.splitext(os.path.split((urlparse(image['hdurl'])).path)[1])[0],
                           extension_returner(image['hdurl']), "images")
            except KeyError:
                youtube_check = urlparse(image['url'])
                if youtube_check.netloc == 'www.youtube.com':
                    pass
                else:
                    save_img(image['url'], os.path.splitext(os.path.split((urlparse(image['url'])).path)[1])[0],
                               extension_returner(image['url']), "images")
    else:
        try:
            save_img(image_response['hdurl'],
                       os.path.splitext(os.path.split((urlparse(image_response['hdurl'])).path)[1])[0],
                       extension_returner(image_response['hdurl']), "images")
        except KeyError:
            youtube_check = urlparse(image_response['url'])
            if youtube_check.netloc == 'www.youtube.com':
                pass
            else:
                save_img(image_response['url'],
                           os.path.splitext(os.path.split((urlparse(image_response['url'])).path)[1])[0],
                           extension_returner(image_response['url']), "images")


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
    args_parser()


if __name__ == '__main__':
    main()
