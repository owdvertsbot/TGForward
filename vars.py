import os

class config(object):
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    FROM_CHANNEL_ID = os.environ.get("FROM_CHANNEL_ID", None)
    TO_CHANNEL_ID = os.environ.get("TO_CHANNEL_ID", None)
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)
