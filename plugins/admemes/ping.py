#Aadhi000_©

"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from Aadhi import StartTime

@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  botstats = f'<b>Bot Uptime:</b> {currentTime}'           
  await update.reply_text(botstats)
