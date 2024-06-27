import os
import argparse
from connection_errors import requests_retries


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Скрипт сохраняет изображения'
    )
    parser.add_argument("-u", "--url", required=True,
                        help="Url адрес откуда скачивать изображение")
    parser.add_argument("-f", "--filename", required=True,
                        help="Название файла для изображения")
    parser.add_argument("-if", "--img_format", default="jpeg",
                        help="Формат файла для изображения. Пример: .format")
    parser.add_argument("-pa", default="images",
                        help="Путь к папке куда сохраняются изображения")
    parser.add_argument("-pl", "--payload", help="params для url адреса в GET запросе")
    return parser.parse_args()


def save_img(url, filename, image_format="jpeg", path="images", payload=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if path == "images":
        full_path = os.path.join(script_dir, path, f"{filename}")
    else:
        full_path = os.path.join(path, f"{filename}")
    os.makedirs(path, exist_ok=True)
    response = requests_retries(url, params=payload)
    response.raise_for_status()
    with open(f"{full_path}{image_format}", 'wb') as file:
        file.write(response.content)


def main():
    args = parse_arguments()
    save_img(args.url, args.filename, args.img_format, args.pa, args.payload)


if __name__ == '__main__':
    main()
