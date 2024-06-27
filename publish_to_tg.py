import os
import random
import telegram
import time
import argparse
from pathlib import Path
from configure_keys import load_keys
from telegram.error import NetworkError


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", default="4", type=float, help="Задаёт время в часах между публикациями"
                                                            " в Telegram канале. По умолчанию составляет 4 часа")
    parser.add_argument("-p", default=None,
                        help="Публикует указанную фотографию в канал")
    parser.add_argument("-pa", type=str, default="images", help="Путь к папке откуда загружаются фото")
    return parser.parse_args()


def convert_hours_to_seconds(time_s=4):
    return 3600 * time_s


def publish_selected_photo(file_name, image_path, channel, token):
    os.makedirs(image_path, exist_ok=True)
    for path in Path(image_path).rglob('{}.{}'.format(file_name, "*")):
        if path.stem == file_name:
            trying_send_photo(channel, open_file(path.resolve()), token)


def publish_random_photo(time_sleep, image_path, channel, token):
    os.makedirs(image_path, exist_ok=True)
    while True:
        full_path = os.path.join(image_path, random.choice(os.listdir(image_path)))
        trying_send_photo(channel, open_file(full_path), token)
        time.sleep(time_sleep)


def open_file(file):
    with open(file, 'rb') as photo:
        return photo.read()


def trying_send_photo(load_key, photo_data, token):
    bot = telegram.Bot(token=token)
    retries = 0
    for attempt in range(31):
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
    tg_channel = load_keys("TG_CHANNEL")
    tg_key = load_keys("TG_KEY")
    args = parse_arguments()
    if args.p:
        publish_selected_photo(file_name=args.p, image_path=args.pa, channel=tg_channel, token=tg_key)
        time.sleep(convert_hours_to_seconds(time_s=args.t))
        publish_random_photo(convert_hours_to_seconds(time_s=args.t), image_path=args.pa, channel=tg_channel,
                             token=tg_key)
    else:
        publish_random_photo(convert_hours_to_seconds(time_s=args.t), image_path=args.pa, channel=tg_channel,
                             token=tg_key)


if __name__ == "__main__":
    main()
