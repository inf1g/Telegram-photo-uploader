import subprocess
import sys
import telegram
from configure_keys import load_keys


def tg_bot():
    bot = telegram.Bot(token=load_keys("TG_KEY"))
    print(bot.get_me())


def main():
    tg_bot()
    # id = 1
    # args = [f"-id {id}"]
    # if id:
    #     subprocess.call([sys.executable, "fetch_spacex_images.py"] + args)
    # else:
    #     subprocess.call([sys.executable, "fetch_spacex_images.py"])
    #
    # subprocess.call([sys.executable, "fetch_nasa_epic_images.py"] + args)
    # subprocess.call([sys.executable, "fetch_nasa_apod_images.py"] + args)

# "-id", help="Загрузит фото от SpaceX по указанному ID запуска")
# "-d", "--date", help="Загрузит EPIC-фото от NASA за указаный день в формате 2024-06-15")
# "-d", "--date", help="Загрузит APOD-фото от NASA за указаный день в формате 2024-06-15")
if __name__ == "__main__":
    main()
