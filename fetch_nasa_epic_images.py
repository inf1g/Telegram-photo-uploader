import argparse
from configure_keys import load_keys
from images_saver import save_img
from connection_errors import secure_request
from datetime import datetime


def args_parser():
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
        payload = {
            "api_key": token
        }
        response = secure_request(url, params=payload)
    else:
        url = "https://api.nasa.gov/EPIC/api/natural/images"
        payload = {
            "api_key": token
        }
        response = secure_request(url, params=payload)
    response.raise_for_status()
    return response.json()


def main():
    args = args_parser()
    payload = {"api_key": load_keys("NASE_KEY")}
    for image in request_nasa(load_keys("NASE_KEY"), date=args.d):
        date = (image["date"])
        year = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%Y')
        month = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%m')
        day = datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%d')
        url = f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/png/{image["image"]}.png"
        save_img(url, image["image"], ".png", path=args.pa, payload=payload)


if __name__ == '__main__':
    main()
