"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from Aadhi import StartTime
from utils_bot import *
@Client.on_message(filters.command('ping') & filters.private & ~filters.edited)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@Client.on_message(filters.command('stats') & filters.private & ~filters.edited)
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  botstats = f'<b>Bot Uptime:</b> {currentTime}'           
  await update.reply_text(botstats)
