# ::: WARNING :::
# THIS IS NOT A KANGED SCRIPT AND THIS IS FULLY CODED BY @ANJANA-MA.
# @AmarnathCJD HE IS HELP ME TO MAKE THIS SCRIPT. 
# ALRIGHTS RESERVED.

import os
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import heroku
from plugins.forward import forward

logging.basicConfig(level=logging.INFO)

AnjanaMa = TelegramClient(StringSession(heroku.STRING_SESSION),
                  				api_id=heroku.API_ID,
                  				api_hash=heroku.API_HASH)

AnjanaMa.start()
AnjanaMa.loop.run_until_complete(forward())
