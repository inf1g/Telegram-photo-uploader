import argparse
import os
from urllib.parse import urlparse
from configure_keys import load_keys
from images_saver import save_img
from file_extension import extension_returner
from connection_errors import secure_request


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт загружает и сохраняет Последние APOD-фото от NASA'
    )
    parser.add_argument("-da", default=None,
                        help="Загрузит APOD-фото от NASA за указанный день в формате 2024-06-15")
    parser.add_argument("-pa", default="images",
                        help="Путь к папке куда сохраняются изображения.")
    parser.add_argument("-am", default="30",
                        help="Количество скачиваемых фото до 50 шт.")
    return parser.parse_args()


def request_nasa(token, date, amount):
    url = "https://api.nasa.gov/planetary/apod"
    if not date:
        payload = {
            "api_key": token,
            "count": amount
        }
    else:
        payload = {
            "api_key": token,
            "date": {date}
        }
    response = secure_request(url, params=payload)
    response.raise_for_status()
    return response.json()


def check_url(json, path):
    try:
        img_url = json['hdurl']
        save_img(img_url,
                 os.path.splitext(os.path.split((urlparse(img_url)).path)[1])[0],
                 extension_returner(img_url), path)
    except KeyError:
        pass


def main():
    args = args_parser()
    image_response = request_nasa(load_keys("NASE_KEY"), date=args.da, amount=args.am)
    if isinstance(image_response, list):
        for image in image_response:
            check_url(image, path=args.pa)
    else:
        check_url(image_response, args.pa)


if __name__ == '__main__':
    main()
