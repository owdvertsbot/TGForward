# ::: WARNING :::
# THIS IS NOT A KANGED SCRIPT AND THIS IS FULLY CODED BY @ANJANA-MA.
# @AmarnathCJD HE IS HELP ME TO MAKE THIS SCRIPT. 
# ALRIGHT RESERVED.

import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterMusic, InputMessagesFilterVideo, InputMessagesFilterPhotos
from telethon.errors import FloodError
from vars import config

api_id = config.API_ID
api_hash = config.API_HASH
from_chat = config.FROM_CHANNEL_ID
to_chat = config.TO_CHANNEL_ID
custom_caption = config.CUSTOM_CAPTION
file_type = config.FILE_TYPE
bot = TelegramClient(StringSession(config.STRING_SESSION), api_id, api_hash)

bot.start()

print("Please wait starting forwarding")
print("Start auto forwarding....")

async def forward():
  mode = None
  if file_type == "docs":
    print("Now forwarding only documents")
    mode = InputMessagesFilterDocument
  elif file_type == "music":
    print("Now forwarding only music")
    mode=InputMessagesFilterMusic
  elif file_type == "videos":
    print("Now forwarding only videos")
    mode=InputMessagesFilterVideo
  elif file_type == "photos":
    print("Now forwarding only photos")
    mode=InputMessagesFilterPhotos
  elif file_type == "all":
    print("Now forwarding all messages")
  else:
    print("Now forwarding all messages")
  async for msg in bot.iter_messages(from_chat, reverse=True, filter=mode):
      try:
        await asyncio.sleep(2)
        bot.parse_mode = 'html'
        k = await bot.send_file(to_chat, file=msg.media, caption=custom_caption)
      except FloodError as e:
        asyncio.sleep(e.seconds)

bot.loop.run_until_complete(forward())
bot.run_until_disconnected()
