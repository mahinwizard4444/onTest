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
    rm = await message.reply_text("•••")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    uptime = time.strftime("%Hh | %Mm | %Ss", time.gmtime(time.time() - BOT_START_TIME))
    await rm.edit(       
        "༺ᴄᴜʀʀᴇɴᴛ ʙᴏᴛ sᴛᴀᴛᴜs༻\n\n"  
        f"‹› ᴘᴏɴʜ : {time_taken_s:.3f} ms",     
        f"‹› ɴᴏᴛ ᴜᴘᴛɪᴍᴇ : {uptime}\n",  
        quote=True,        
        parse_mode="md"
    )
    await rm.edit(       
        "༺ᴄᴜʀʀᴇɴᴛ ʙᴏᴛ sᴛᴀᴛᴜs༻\n\n"  
        f"‹› ᴘᴏɴʜ :{time_taken_s:.3f} ms",     
        f"‹› ɴᴏᴛ ᴜᴘᴛɪᴍᴇ : {uptime}\n",   
        quote=True,
        parse_mode="md"
    )
