# ::: WARNING :::
# THIS IS NOT A KANGED SCRIPT AND THIS IS FULLY CODED BY @ANJANA-MA.
# @AmarnathCJD HE IS HELP ME TO MAKE THIS SCRIPT. 
# ALRIGHTS RESERVED.

import os
import logging
from telethon import TelegramClient
from telethon.sessions import StringSession
from config import heroku

logging.basicConfig(level=logging.INFO)

AnjanaMa = Client('AnjanaMa',
                  api_id=Config.API_ID,
                  api_hash=Config.API_HASH,
                  bot_token=Config.BOT_TOKEN,
                  plugins=dict(root="plugins"))

AnjanaMa.run()