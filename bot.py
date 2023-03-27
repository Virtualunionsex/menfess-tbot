# File ini bagian dari Repositori: github.com/raflydtya/menfess-tbot Akun: @raflydtya
# Nama: bot.py | Python Telegram Bot
# Copyright 2022. All Right Reserved.

import html
import time, asyncio, sys, random, inspect, re, logging
from telethon import TelegramClient, events, utils
from typing import Optional

api_id = 16246834
api_hash = '29b3ffa9245c07f05375b92f38e8f13d'
sesi_file = 'menfess executive'
bot_token = '5990927168:AAE3uVXTDPT-zviopBCNMST9m4LABCM97xM'

menfessbot = TelegramClient(sesi_file, api_id, api_hash).start(bot_token=bot_token)

group = '<t.me/executive_fams>'
ch = '<t.me/+U1NZZ_oK_j1kNjM1>'

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
  TEXT+= f"Ini adalah bot Menfess executive di Telegram. Kirim pesanmu dengan trigger (#exe), maka pesanmu akan terkirim ke (https://t.me/+ETSJ66ZlMfZhNTJl)"
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
