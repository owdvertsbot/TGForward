# ::: WARNING :::
# THIS IS NOT A KANGED SCRIPT AND THIS IS FULLY CODED BY @ANJANA-MA.
# @AmarnathCJD HE IS HELP ME TO MAKE THIS SCRIPT. 
# ALRIGHT RESERVED.

import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputMessagesFilterDocument
from telethon.errors import FloodError
from vars import config

api_id = config.API_ID
api_hash = "{config.API_HASH}"
bot = TelegramClient(StringSession("{config.STRING_SESSION}"), api_id, api_hash)

bot.start()

async def forward():
  async for msg in bot.iter_messages(config.FROM_CHANNEL_ID, reverse=True, filter=InputMessagesFilterDocument):
    try:
      await asyncio.sleep(1)
      k = await client.send_file(config.TO_CHANNEL_ID, file=msg.media, caption="{config.CUSTOM_CAPTION}")
    except FloodError as e:
      asyncio.sleep(e.seconds)
bot.loop.run_until_complete(clone())
bot.run_until_disconnected()