# File ini bagian dari Repositori: github.com/raflydtya/menfess-tbot Akun: @raflydtya
# Nama: bot.py | Python Telegram Bot
# Copyright 2022. All Right Reserved.

import html
import time, asyncio, sys, random, inspect, re, logging
from telethon import TelegramClient, events, utils
from typing import Optional

api_id = isi api id milikmu 
api_hash = 'isi api hash milikmu'
sesi_file = 'menfessbot'
bot_token = 'isi bot api token'

menfessbot = TelegramClient(sesi_file, api_id, api_hash).start(bot_token=bot_token)

group = '<username grup telegram>'
ch = '<username channel telegram>'

def menfess(**args):
    pattern = args.get("pattern", None)

    r_pattern = r"^[/!.]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        client.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator

FOTO = "<https://telegra.ph/file/86efaa73273481ab9f48a.jpg>"
@menfess(pattern=("/start"))
async def start(event):
  TEXT = f"Halo {event.sender.first_name}!\n"
  TEXT+= f"Ini adalah bot Menfess executive di Telegram. Kirim pesanmu dengan trigger (#exe), maka pesanmu akan terkirim ke (https://t.me/+ETSJ66ZlMfZhNTJl)()"
  BUTTON = [[Button.url("Grup", group)]]
  await bot.send_file(event.chat_id, FOTO, caption=TEXT, buttons=BUTTON )
  print(time.asctime(), '|', event.sender.first_name, '|', event.sender.username, '|', event.sender.id, '|', 'Started Bot' )

@menfessbot.on(events.NewMessage)
async def handler(event):
        pesan = event.raw_text
 
         if '<isi trigger>' in pesan:
            time.sleep(0.5)
            await bot.send_message(<group/ch>, pesan)
            return

with menfessbot:
    print(time.asctime(), '-', '--BOT STARTED--')
    menfessbot.run_until_disconnected()
