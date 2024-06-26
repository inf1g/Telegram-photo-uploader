import os
from dotenv import load_dotenv


def load_keys(token):
    load_dotenv()
    key = os.environ[token]
    return key
