import os
from urllib.parse import urlparse


def extension_returner(url):
    return os.path.splitext(urlparse(url).path)[1]
