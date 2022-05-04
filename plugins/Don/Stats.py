#@Aadhi000 #AVR

import os
import math
import time
import heroku3
import requests
from plugins.helper_functions.cust_p_filters import f_onw_fliter
from pyrogram import Client, filters
from database.users_chats_db import db
from info import COMMAND_HAND_LER

#=====================================================
BOT_START_TIME = time.time()

HEROKU_API_KEY = (os.environ.get("HEROKU_API_KEY", ""))
#=====================================================

@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()  
    avr = await message.reply_text("•••")  
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))   
    await avr.edit(f"-𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂-\n\n‹› 𝙿𝙾𝙽𝙶! : {time_taken_s:.3f} ms\n‹› 𝙱𝙾𝚃 𝚄𝙿𝚃𝙸𝙼𝙴 : {uptime}")        


