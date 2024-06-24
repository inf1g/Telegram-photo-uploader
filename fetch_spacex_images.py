import argparse
import os
from urllib.parse import urlparse
from images_saver import save_img
from file_extension import extension_returner
from connection_errors import secure_request


def args_parser():
    parser = argparse.ArgumentParser(description='Скрипт загружает и сохраняет фото от SpaceX')
    parser.add_argument("-id", default="6243ad8baf52800c6e919252",
                        help="Загрузит фото от SpaceX по-указанному ID запуска")
    parser.add_argument("-pa", default="images",
                        help="Путь к папке куда сохраняются изображения")
    return parser.parse_args()


def request_spacex(launch_id):
    response = secure_request(f"https://api.spacexdata.com/v5/launches/{launch_id}")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def main():
    args = args_parser()
    for image in request_spacex(launch_id=args.id):
        save_img(image, (os.path.splitext(os.path.split((urlparse(image)).path)[1])[0]),
                 extension_returner(image), path=args.pa)


if __name__ == '__main__':
    main()
