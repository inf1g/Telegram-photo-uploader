import json
import datetime
import requests
import os
from urllib.parse import urlparse
from dotenv import load_dotenv


def configure_keys(token):
    load_dotenv()
    key = os.getenv(token)
    return key


def spacex_request():
    response = requests.get("https://api.spacexdata.com/v5/launches/6243ad8baf52800c6e919252")
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def nasa_planetary_requests(token):
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": token,
        "count": "30"
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def nasa_epic_requests(token):
    # url = (f"https://api.nasa.gov/EPIC/archive/natural/{year}/{month}/{day}/jpg/{image_name}.jpg")
    # payload = {
    #     "api_key": token
    # }
    # response = requests.get(url, params=payload)
    # response.raise_for_status()
    # print(response.text)
    # return
    with open(f"D:\\321.json", "r") as f:
        data = json.load(f)
        for image in data:
            image_name = image["image"]
            print(image["date"].split(" ")[0])
            date = datetime.date.fromisoformat(image["date"].split(" ")[0])

            year = image["date"].split("-")[0]
            month = image["date"].split("-")[1]
            day = image["date"].split("-")[2].split(" ")[0]
            url2 = (f"https://api.nasa.gov/EPIC/archive/natural/{date.year}/{date.month}/{date.day}/png/{image_name}.png")
            print(url2)


def file_extension(url):
    return os.path.splitext(urlparse(url).path)[1]


def saving_images(url, filename, image_format="jpeg", path="images\\"):
    os.makedirs(f"{path}", exist_ok=True)
    response = requests.get(url)
    response.raise_for_status()
    with open(f"{path}{filename}.{image_format}", 'wb') as file:
        file.write(response.content)


def main():
    nasa_token = configure_keys("NASE_KEY")
    path = "images_nasa\\"
    # for image_name, image_url in enumerate(spacex_request()):
    #     saving_images(image_url, image_name, file_extension(image_url))
    # for image in nasa_planetary_requests(nasa_token):
    #     try:
    #         print(image["hdurl"])
    #         saving_images(image["hdurl"], os.path.splitext(os.path.split((urlparse(image["hdurl"])).path)[1])[0],
    #                       file_extension(image["hdurl"]), path)
    #     except KeyError:
    #         print(image["url"])
    #         saving_images(image["url"], os.path.splitext(os.path.split((urlparse(image["url"])).path)[1])[0],
    #                       file_extension(image["url"]), path)

    nasa_epic_requests(nasa_token)




if __name__ == '__main__':
    main()
