import os
from urllib.parse import urlparse


def returns_extension(url):
    return os.path.splitext(urlparse(url).path)[1]
