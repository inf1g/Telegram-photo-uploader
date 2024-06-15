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
    nasa_token = load_keys("NASE_KEY")
    payload = {"api_key": nasa_token}
    if args.date:
        nasa_epic_req_pars = nasa_epic_requests(nasa_token, date=args.date)
    else:
        nasa_epic_req_pars = nasa_epic_requests(nasa_token)
    for image in nasa_epic_req_pars:
        image_name = image["image"]
        date = datetime.date.fromisoformat(image["date"].split(" ")[0])
        month = image["date"].split("-")[1]
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{month}/{date.day}/png/{image_name}.png"
        saving_img(url, image_name, "png", "images_nasa_EPIC\\", payload)


def nasa_epic_requests(token, date=None):
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
