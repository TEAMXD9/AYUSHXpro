from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("CʜᴀᴛGPT᭄🪽", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("ɢʀᴏᴜᴘs᭄🪽", callback_data="mplus HELP_Group"),InlineKeyboardButton("sᴛɪᴄᴋᴇʀs᭄🪽", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("Tᴀɢ-Aʟʟ᭄🪽", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("Iɴꜰᴏ᭄🪽", callback_data="mplus HELP_Info"),InlineKeyboardButton("Exᴛʀᴀ᭄🪽", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("Iᴍᴀɢᴇ᭄🪽", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("Aᴄᴛɪᴏɴ᭄🪽", callback_data="mplus HELP_Action"),InlineKeyboardButton("Sᴇᴀʀᴄʜ᭄🪽", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("ғᴏɴᴛ᭄🪽", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("ɢᴀᴍᴇs᭄🪽", callback_data="mplus HELP_Game"),InlineKeyboardButton("Ⓣ-ɢʀᴀᴘʜ᭄🪽", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("ɪᴍᴘᴏsᴛᴇʀ᭄🪽", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("Tʀᴜᴛʜ-ᗪᴀʀᴇ᭄🪽", callback_data="mplus HELP_TD"),InlineKeyboardButton("ʜᴀsᴛᴀɢ᭄🪽", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("ᴛᴛs᭄🪽", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("ғᴜɴ᭄🪽", callback_data="mplus HELP_Fun"),InlineKeyboardButton("ǫᴜᴏᴛʟʏ᭄🪽", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("<", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton(">", callback_data=f"managebot123 settings_back_helper"),
    ]]