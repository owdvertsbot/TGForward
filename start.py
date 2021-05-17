# ::: WARNING :::
# THIS IS NOT A KANGED SCRIPT AND THIS IS FULLY CODED BY @ANJANA-MA.
# @AmarnathCJD HE IS HELP ME TO MAKE THIS SCRIPT. 
# ALRIGHTS RESERVED.

import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import heroku

logging.basicConfig(level=logging.INFO)

AnjanaMa = TelegramClient(StringSession(heroku.STRING_SESSION),
                  				api_id=heroku.API_ID,
                  				api_hash=heroku.API_HASH,
                  				root="plugins")

AnjanaMa.run()