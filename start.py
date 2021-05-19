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

api_id = heroku.API_ID
api_hash = heroku.API_HASH
bot_token = heroku.BOT_TOKEN

AnjanaMa = TelegramClient('AnjanaMa', api_id, api_hash).start(bot_token=bot_token)

with AnjanaMa:
    AnjanaMa.loop.run_until_complete(forward())
