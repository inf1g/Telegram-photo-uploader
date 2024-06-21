import requests
import argparse
import os
from urllib.parse import urlparse
from images_saver import saving_img
from file_extension import extension_returner


def args_parser():
    parser = argparse.ArgumentParser(description='Скрипт загружает и сохраняет фото от SpaceX')
    parser.add_argument("-id", default="6243ad8baf52800c6e919252",
                        help="Загрузит фото от SpaceX по-указанному ID запуска")
    args = parser.parse_args()
    for image in spacex_request(idl=args.id):
        saving_img(image, (os.path.splitext(os.path.split((urlparse(image)).path)[1])[0]),
                   extension_returner(image))


def spacex_request(idl):
    response = requests.get(f"https://api.spacexdata.com/v5/launches/{idl}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    args_parser()


if __name__ == '__main__':
    main()
