import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class config(object):
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    STRING_SESSION = os.getenv("STRING_SESSION")
    FROM_CHANNEL_ID = os.getenv("FROM_CHANNEL_ID")
    TO_CHANNEL_ID = os.getenv("TO_CHANNEL_ID")
    CUSTOM_CAPTION = os.getenv("CUSTOM_CAPTION")