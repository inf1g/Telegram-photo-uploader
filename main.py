import subprocess
import argparse


def args_parser():
    parser = argparse.ArgumentParser("В этом файле устанавливаются флаги для остальных скриптов")
    parser.add_argument("-t", default="4", help="Задаёт время в часах между публикациями"
                                                " в Telegram канале. По умолчанию составляет 4 часа")
    parser.add_argument("-id", default="6243ad8baf52800c6e919252",
                        help="Загрузит фото от SpaceX по-указанному ID запуска")
    parser.add_argument("-d", default=None,
                        help="Загрузит EPIC-фото от NASA за указанный день в формате 2024-06-15")
    parser.add_argument("-da", default=None,
                        help="Загрузит APOD-фото от NASA за указанный день в формате 2024-06-15")
    parser.add_argument("-p", help="Публикует указанную фотографию в канал")
    parser.add_argument("-pa", help="Путь к папке куда сохраняются изображения")
    parser.add_argument("-am", default="30",
                        help="Количество скачиваемых фото до 50 шт.")
    args = parser.parse_args()
    return args


def run_subprocess(script_name, args_list):
    if args_list:
        subprocess.run(['python', script_name] + args_list)
    else:
        subprocess.run(['python', script_name])


def check_and_runs_args(args):
    scripts_args = {
        'fetch_spacex_images.py': [('id', '-id'), ('pa', '-pa')],
        'fetch_nasa_epic_images.py': [('d', '-d'), ('pa', '-pa')],
        'fetch_nasa_apod_images.py': [('da', '-da'), ('pa', '-pa'), ('am', '-am')],
        'publish_to_tg.py': [('t', '-t'), ('p', '-p'), ('pa', '-pa')]
    }
    for script, arg_keys in scripts_args.items():
        script_args = []
        for attr, flag in arg_keys:
            if getattr(args, attr):
                script_args.extend([flag, getattr(args, attr)])
        run_subprocess(script, script_args)


def main():
    check_and_runs_args(args_parser())


if __name__ == "__main__":
    main()
