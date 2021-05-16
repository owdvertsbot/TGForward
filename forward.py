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
api_hash = config.API_HASH
from_chat = config.FROM_CHANNEL_ID
to_chat = config.TO_CHANNEL_ID
custom_caption = config.CUSTOM_CAPTION
bot = TelegramClient(StringSession(config.STRING_SESSION), api_id, api_hash)

bot.start()

print("Please wait starting forwarding")
print("Start auto forwarding....")

async def forward():
  async for msg in bot.iter_messages(from_chat, reverse=True, filter=InputMessagesFilterDocument):
    try:
      await asyncio.sleep(1)
      bot.parse_mode = 'html'
      k = await bot.send_file(to_chat, file=msg.media, caption=custom_caption)
    except FloodError as e:
      asyncio.sleep(e.seconds)
bot.loop.run_until_complete(forward())
bot.run_until_disconnected()
