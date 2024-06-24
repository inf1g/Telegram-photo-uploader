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
    parser.add_argument("-p", help="Публикует указанную фотографию в канал")
    parser.add_argument("-pa", help="Путь к папке куда сохраняются изображения")
    parser.add_argument("-am", default="30",
                        help="Количество скачиваемых фото до 50 шт.")
    args = parser.parse_args()
    return args


def check_args(args):
    fetch_spacex_images_args = []
    if args.id:
        fetch_spacex_images_args.extend(['-id', args.id])
    if args.pa:
        fetch_spacex_images_args.extend(['-pa', args.pa])
    subprocess.run(['python', 'fetch_spacex_images.py'] + fetch_spacex_images_args)
    if not any([args.id, args.pa]):
        subprocess.call(['python', 'fetch_spacex_images.py'])
    fetch_nasa_epic_images_args = []
    if args.d:
        fetch_nasa_epic_images_args.extend(['-d', args.d])
    if args.pa:
        fetch_nasa_epic_images_args.extend(['-pa', args.pa])
    subprocess.run(['python', 'fetch_nasa_epic_images.py'] + fetch_nasa_epic_images_args)
    if not any([args.d, args.pa]):
        subprocess.call(['python', 'fetch_nasa_epic_images.py'])
    fetch_nasa_apod_images_args = []
    if args.da:
        fetch_nasa_apod_images_args.extend(['-da', args.da])
    if args.pa:
        fetch_nasa_apod_images_args.extend(['-pa', args.pa])
    if args.am:
        fetch_nasa_apod_images_args.extend(['-am', args.am])
    subprocess.run(['python', 'fetch_nasa_apod_images.py'] + fetch_nasa_apod_images_args)
    if not any([args.da, args.pa, args.am]):
        subprocess.call(['python', 'fetch_nasa_apod_images.py'])
    publishing_to_tg_args = []
    if args.t:
        publishing_to_tg_args.extend(['-t', args.t])
    if args.p:
        publishing_to_tg_args.extend(['-p', args.p])
    if args.pa:
        publishing_to_tg_args.extend(['-pa', args.pa])
    subprocess.call(['python', 'publishing_to_tg.py'] + publishing_to_tg_args)
    print(publishing_to_tg_args)
    if not any([args.p, args.pa, args.t]):
        subprocess.call(['python', 'publishing_to_tg.py'])


def main():
    check_args(args_parser())


if __name__ == "__main__":
    main()
