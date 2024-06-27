import time
import requests
from requests.exceptions import ConnectionError


def requests_retries(url, params=None, max_retries=30, retry_delay=10, quick_retry_delay=1):
    retries = 0
    for attempt in range(max_retries):
        try:
            response = requests.get(url, params=params)
            if response.ok:
                return response
        except ConnectionError:
            if retries == 0:
                time.sleep(quick_retry_delay)
            else:
                time.sleep(retry_delay)
            retries += 1
