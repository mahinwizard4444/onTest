#@Aadhi000 #AVR #neo

import asyncio
import os
import math
import time
import heroku3
import requests
from pyrogram import Client, filters

#=====================================================
BOT_START_TIME = time.time()
#=====================================================

@Client.on_message(filters.command("ping"))
async def ping(_, message):
    start_t = time.time()  
    avr = await message.reply_text("β’β’β’")  
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))   
    await avr.edit(f"-π²ππππ΄π½π π±πΎπ πππ°πππ-\n\nβΉβΊ πΏπΎπ½πΆ! : {time_taken_s:.3f} ms\nβΉβΊ π±πΎπ ππΏππΈπΌπ΄ : {uptime}")
    await asyncio.sleep(10)
    await avr.delete()
