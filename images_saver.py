import requests
import os
import argparse


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт сохраняет изображения'
    )
    parser.add_argument("-u", "--url", required=True,
                        help="Url адресс откуда скачивать изображение")
    parser.add_argument("-f", "--filename", type=str, required=True,
                        help="Название файла для изображения")
    parser.add_argument("-if", "--img_format", help="Название файла для изображения")
    parser.add_argument("-p", "--path", type=str, help="название папки куда сохраняются изображения")
    parser.add_argument("-pl", "--payload", help="params для url адреса в GET запросе")
    args = parser.parse_args()
    saving_img(args.url, args.filename, args.img_format, args.path, args.payload)


def saving_img(url, filename, image_format="jpeg", path="images\\", payload=()):
    file_path = os.path.realpath(__file__)
    script_dir = os.path.dirname(file_path)
    os.makedirs(f"{script_dir}\\{path}\\", exist_ok=True)
    response = requests.get(url, params=payload)
    response.raise_for_status()
    with open(f"{script_dir}\\{path}\\{filename}{image_format}", 'wb') as file:
        file.write(response.content)


def main():
    args_parser()


if __name__ == '__main__':
    main()
