import subprocess
import argparse


def args_parser():
    parser = argparse.ArgumentParser("В этом файле устанавливаются флаги для остальных скриптов")
    parser.add_argument("-t", default="4", help="Задаёт время в часах между публикациями"
                                                " в Telegram канале. По умолчанию составляет 4 часа")
    parser.add_argument("-id", default="6243ad8baf52800c6e919252",
                        help="Загрузит фото от SpaceX по-указанному ID запуска")
    parser.add_argument("-d", default=None,
                        help="Загрузит EPIC-фото от NASA за указаный день в формате 2024-06-15")
    parser.add_argument("-da", default=None,
                        help="Загрузит APOD-фото от NASA за указаный день в формате 2024-06-15")
    parser.add_argument("-p", default="51981688502_0584ac5658_o", help="Публикует указанную фотографию в канал")
    args = parser.parse_args()
    if args.id:
        subprocess.call(['python', 'fetch_spacex_images.py', '-id', args.id])
    if not args.id:
        subprocess.call(['python', 'fetch_spacex_images.py'])
    if args.d:
        subprocess.call(['python', 'fetch_nasa_epic_images.py', '-d', args.d])
    if not args.d:
        subprocess.call(['python', 'fetch_nasa_epic_images.py'])
    if args.da:
        subprocess.call(['python', 'fetch_nasa_apod_images.py', '-da', args.da])
    if not args.da:
        subprocess.call(['python', 'fetch_nasa_apod_images.py'])
    if args.t:
        subprocess.call(['python', 'tg_bot.py', '-t', args.t])
    if not args.t:
        subprocess.call(['python', 'tg_bot.py'])
    if args.p:
        subprocess.call(['python', 'tg_bot.py', '-p', args.p])
    if not args.p:
        subprocess.call(['python', 'tg_bot.py'])


def main():
    args_parser()


if __name__ == "__main__":
    main()
