import time
import requests
from requests.exceptions import ConnectionError


def secure_request(url, params="", max_retries=30, retry_delay=10, quick_retry_delay=1):
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response
            else:
                pass
        except ConnectionError:
            if retries == 0:
                time.sleep(quick_retry_delay)
            else:
                time.sleep(retry_delay)
            retries += 1


def main():
    pass


if __name__ == '__main__':
    main()
