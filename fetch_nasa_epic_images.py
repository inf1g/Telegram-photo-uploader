import requests
import argparse
import datetime
from configure_keys import load_keys
from images_saver import saving_img


def args_parser():
    parser = argparse.ArgumentParser(
        description='Скрипт загружает и сохраняет Последние EPIC-фото от NASA'
    )
    parser.add_argument("-d", "--date", help="Загрузит EPIC-фото от NASA за указаный день в формате 2024-06-15")
    args = parser.parse_args()
    payload = {"api_key": load_keys("NASE_KEY")}
    if args.date:
        nasa_epic_req_pars = nasa_requests(load_keys("NASE_KEY"), date=args.date)
    else:
        nasa_epic_req_pars = nasa_requests(load_keys("NASE_KEY"))
    for image in nasa_epic_req_pars:
        date = datetime.date.fromisoformat(image["date"].split(" ")[0])
        month = image["date"].split("-")[1]
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{month}/{date.day}/png/{image["image"]}.png"
        saving_img(url, image["image"], ".png", "images\\", payload)


def nasa_requests(token, date=None):
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
