# ::: WARNING :::
# THIS IS NOT A KANGED SCRIPT AND THIS IS FULLY CODED BY @ANJANA-MA.
# @AmarnathCJD HE IS HELP ME TO MAKE THIS SCRIPT. 
# ALRIGHTS RESERVED.

import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import heroku
from plugins.forward import forward

logging.basicConfig(level=logging.INFO)

AnjanaMa = TelegramClient('AnjanaMa',
                  api_id=config.API_ID,
                  api_hash=config.API_HASH,
                  bot_token=config.BOT_TOKEN)

AnjanaMa.start()
AnjanaMa.loop.run_until_complete(forward())
