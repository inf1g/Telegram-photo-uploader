import requests
import os
import argparse


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт сохраняет изображения'
    )
    parser.add_argument("-u", "--url", required=True,
                        help="Url адресс откуда скачивать изображение")
    parser.add_argument("-f", "--filename", required=True,
                        help="Название файла для изображения")
    parser.add_argument("-if", "--img_format", help="Формат файла для изображения. Пример: .format")
    parser.add_argument("-p", "--path", help="Название папки куда сохраняются изображения")
    parser.add_argument("-pl", "--payload", help="params для url адреса в GET запросе")
    args = parser.parse_args()
    save_img(args.url, args.filename, args.img_format, args.path, args.payload)


def save_img(url, filename, image_format="jpeg", path="images", payload=()):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(script_dir, path, f"{filename}.{image_format}")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(full_path, 'wb') as file:
        file.write(response.content)


def main():
    args_parser()


if __name__ == '__main__':
    main()
