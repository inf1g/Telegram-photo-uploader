## Space Telegram.

Скачивает фото от API SpaceX, NASA и публикует указанную фотографию в канал. Если “какую” не указано, публикует случайную фотографию. Публикует все фото из директории в бесконечном раз в 4 часа.
 

## Установка

1. Для запуска должен быть установлен [Python 3](https://www.python.org/downloads/release/python-3124/)
2. Клонируйте репозиторий с github
3. Установите зависимости 
```bash
pip install -r requirements.txt
```
4. Создайте файл `.env` указав имя и значение этой переменной как на примере ниже, замените `0123456789abcdefgh` на свой сервисный ключ – “токен” NASA.
```bash
NASE_KEY=0123456789abcdefgh
```
### Как его получить: 
- NASA APIs — [зарегистрируйтесь](https://api.nasa.gov/)
- Получите токен на почте указанной при регистрации.
---
5. В файл `.env` укажите 'Токен' для Telegram бота как на примере ниже, замените `0123456789abcdefgh` на свой сервисный ключ – “токен” Telegram.
```bash
TG_KEY==0123456789abcdefgh
```
### Как его получить:
- Зарегистрируйтесь в Telegram — [зарегистрируйтесь](https://web.telegram.im/)
- Откройте чат с [@BotFather](https://telegram.me/BotFather).
- Для создания нового бота отправьте команду в чат 
```bash
/newbot
```
- Выберите имя для своего бота и имя пользователя Telegram для вашего бота. Оно должно заканчиваться на bot. 

![Static Badge](https://way23.ru/images/telegram_newbot.png)

- В ответном сообщении приходит токен который нужен для управления ботом через API.


---
#### Укажите Telegram канал куда будут публиковаться фото.

5. В файл `.env` укажите имя вашего канала Telegram, как на примере ниже. Замените @tg_test_channel на имя канала, куда будут публиковаться фото.
```bash
TG_CHANNEL=@tg_test_channel
```

6. Запустите скрипт 'main.py'
```bash
python main.py
```
7. Параметры запуска скрипта 'main.py':
- ` -t` Где 4 - это время в часах между публикациями.
```bash
python main.py -t 4
```
- ` -p ` Где ` epic_1b_20240611134201`  - это название фото, по умолчанию из папки ` image`.
```bash
python main.py -p epic_1b_20240611134201
```
- ` -id ` Загрузит фото от SpaceX по-указанному ID запуска. `6243ad8baf52800c6e919252` - ID запуска с примера ниже.
```bash
python main.py -id 6243ad8baf52800c6e919252
```
- ` -d ` Загрузит EPIC-фото от NASA за указанный день в формате: год месяц день. Пример даты  2024-06-15.
```bash
python main.py -d 2024-06-15
``` 
- ` -da ` Загрузит APOD-фото от NASA за указанный день в формате: год месяц день. Пример даты 2024-06-15.
```bash
python main.py -da 2024-06-15
``` 
- ` -pa ` Где `C:\space_images`  - Путь к папке откуда загружаются фото. Стандартно фото хранятся в папке `images`.
```bash
python main.py -pa C:\space_images
```
- ` -am ` Где `30`  - Количество скачиваемых фото до 50 шт.
```bash
python main.py -am 30
```

## Параметры запуска отдельных скриптов.

#### Для NASA

- ` -da ` Загрузит APOD-фото от NASA за указанный день в формате: год месяц день. Пример даты 2024-06-15.
```bash
python fetch_nasa_apod_images.py -da 2024-06-15
``` 
- ` -am ` Количество скачиваемых фото до 50 шт.
```bash
python fetch_nasa_apod_images.py -am 30
``` 
- ` -d ` Загрузит EPIC-фото от NASA за указанный день в формате: год месяц день. Пример даты 2024-06-15.
```bash
python fetch_nasa_epic_images.py -d 2024-06-15
``` 
- ` -pa ` Где `C:\space_images`  - Путь к папке откуда загружаются фото. Стандартно фото хранятся в папке `images`
```bash
python fetch_nasa_epic_images.py -pa C:\space_images
```
или
```bash
python fetch_nasa_apod_images.py -pa C:\space_images
```

#### Для SpaceX

- ` -id ` Загрузит фото от SpaceX по-указанному ID запуска. `6243ad8baf52800c6e919252` - ID запуска с примера ниже.
```bash
python fetch_spacex_images.py -id 6243ad8baf52800c6e919252
```
- ` -p ` Где `epic_1b_20240611134201`  - это название фото из папки ` image`.
```bash
python fetch_spacex_images.py -p epic_1b_20240611134201
```
- ` -pa ` Где `C:\space_images`  - Путь к папке откуда загружаются фото. Стандартно фото хранятся в папке `images`
```bash
python fetch_spacex_images.py -pa C:\space_images
```

#### Для Telegram 
##### Загрузка в Telegram канал по названию фото.

- ` -p ` Где ` epic_1b_20240611134201`  - это название фото из папки ` image`.
```bash
python publish_to_tg.py -p epic_1b_20240611134201
```
- ` -t ` Где `4`  - Задаёт время в часах между публикациями в Telegram канале. По умолчанию составляет 4 часа.
```bash
python publish_to_tg.py -t 4
```
- ` -pa ` Где `C:\space_images`  - Путь к папке откуда загружаются фото. Стандартно фото хранятся в папке `images`
```bash
python publish_to_tg.py -pa C:\space_images
```
---

## Создано с помощью 

![!Static Badge](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)

## Цель проекта

Код написан в учебных целях - для урока в курсе Python и API веб-сервисов на сайте [Devman](https://dvmn.org/) 
