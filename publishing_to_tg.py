import os
import random
import telegram
import time
import argparse
from pathlib import Path
from configure_keys import load_keys
from telegram.error import NetworkError


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", default="4", type=float, help="Задаёт время в часах между публикациями"
                                                              " в Telegram канале. По умолчанию составляет 4 часа")
    parser.add_argument("-p", default=None,
                        help="Публикует указанную фотографию в канал")
    parser.add_argument("-pa", type=str, default="images", help="Путь к папке откуда загружаются фото")
    return parser.parse_args()


def timer(time_s=4):
    return 3600 * time_s


def publishing_selected_photo(file_name, image_path):
    os.makedirs(image_path, exist_ok=True)
    for path in Path(image_path).rglob(file_name + ".*"):
        if path.stem == file_name:
            with open(f'{path.resolve()}', 'rb') as photo:
                photo_data = photo.read()
                safe_request(load_keys("TG_CHANNEL"), photo_data)


def publishing_random_photo(time_sleep, image_path):
    os.makedirs(image_path, exist_ok=True)
    while True:
        full_path = os.path.join(image_path, random.choice(os.listdir(image_path)))
        with open(full_path, 'rb') as photo:
            photo_data = photo.read()
            safe_request(load_keys("TG_CHANNEL"), photo_data)
            time.sleep(time_sleep)


def safe_request(load_key, photo_data):
    bot = telegram.Bot(token=load_keys("TG_KEY"))
    retries = 0
    while retries < 31:
        try:
            bot.send_photo(chat_id=load_key, photo=photo_data)
            break
        except NetworkError:
            if retries == 0:
                time.sleep(1)
            else:
                time.sleep(10)
            retries += 1


def main():
    args = args_parser()
    if args.p:
        publishing_selected_photo(file_name=args.p, image_path=args.pa)
        time.sleep(timer(time_s=args.t))
        publishing_random_photo(timer(time_s=args.t), image_path=args.pa)
    else:
        publishing_random_photo(timer(time_s=args.t), image_path=args.pa)


if __name__ == "__main__":
    main()
