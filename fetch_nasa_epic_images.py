import argparse
from configure_keys import load_keys
from images_saver import save_img
from connection_errors import requests_retries
from datetime import datetime


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Скрипт загружает и сохраняет Последние EPIC-фото от NASA'
    )
    parser.add_argument("-d", default=None,
                        help="Загрузит EPIC-фото от NASA за указанный день в формате 2024-06-15")
    parser.add_argument("-pa", default="images",
                        help="Путь к папке куда сохраняются изображения")
    return parser.parse_args()


def request_nasa(token, date=None):
    if date:
        url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    else:
        url = "https://api.nasa.gov/EPIC/api/natural/images"
    payload = {
        "api_key": token
    }
    response = requests_retries(url, params=payload)
    response.raise_for_status()
    return response.json()


def main():
    token = load_keys("NASE_KEY")
    args = parse_arguments()
    payload = {"api_key": token}
    for image in request_nasa(token, date=args.d):
        date = image["date"]
        img_dt = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
        url = f"https://api.nasa.gov/EPIC/archive/natural/{img_dt:%Y/%m/%d}/png/{image["image"]}.png"
        save_img(url, image["image"], ".png", path=args.pa, payload=payload)


if __name__ == '__main__':
    main()
