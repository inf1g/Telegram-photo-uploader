import requests
import argparse
from configure_keys import load_keys
from images_saver import save_img


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт загружает и сохраняет Последние EPIC-фото от NASA'
    )
    parser.add_argument("-d", default=None,
                        help="Загрузит EPIC-фото от NASA за указаный день в формате 2024-06-15")
    args = parser.parse_args()
    payload = {"api_key": load_keys("NASE_KEY")}
    for image in request_nasa(load_keys("NASE_KEY"), date=args.d):
        date = (image["date"].split(" ")[0])
        year, month, day = date.split("-")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image["image"]}.png"
        save_img(url, image["image"], ".png", "images", payload)


def request_nasa(token, date=None):
    if date:
        url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"

        payload = {
            "api_key": token
        }
        response = requests.get(url, params=payload)
    else:
        url = "https://api.nasa.gov/EPIC/api/natural/images"

        payload = {
            "api_key": token
        }
        response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def main():
    args_parser()


if __name__ == '__main__':
    main()
