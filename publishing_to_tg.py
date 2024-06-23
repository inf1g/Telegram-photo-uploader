import os
import random
import telegram
import time
import argparse
from pathlib import Path
from configure_keys import load_keys


def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", default="4", type=int, help="Задаёт время в часах между публикациями"
                                                          " в Telegram канале. По умолчанию составляет 4 часа")
    parser.add_argument("-p", default=None,
                        help="Публикует указанную фотографию в канал")
    args = parser.parse_args()
    if args.p:
        publishing_selected_photo(file_name=args.p)
        publishing_random_photo(timer(time_s=args.t))
    else:
        publishing_random_photo(timer(time_s=args.t))


def timer(time_s=4):
    return 3600 * time_s


def publishing_selected_photo(file_name):
    for path in Path("images").rglob(file_name + ".*"):
        if path.stem == file_name:
            bot = telegram.Bot(token=load_keys("TG_KEY"))
            with open(f'{path.resolve()}', 'rb') as photo:
                photo_data = photo.read()
                bot.send_photo(chat_id=load_keys("TG_CHANNEL"), photo=photo_data)


def publishing_random_photo(time_sleep):
    while True:
        bot = telegram.Bot(token=load_keys("TG_KEY"))
        image_path = os.path.join("images", random.choice(os.listdir("images")))
        with open(image_path, 'rb') as photo:
            photo_data = photo.read()
        bot.send_photo(chat_id=load_keys("TG_CHANNEL"), photo=photo_data)
        time.sleep(time_sleep)


def main():
    args_parser()


if __name__ == "__main__":
    main()
