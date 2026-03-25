from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram

class LANG(object):

    START_TEXT = """
<b>👋 Hᴇʏ, {}!</b>\n 
<b>I ᴀᴍ ᴀ ᴘᴏᴡᴇʀғᴜʟ Tᴇʟᴇɢʀᴀᴍ ғɪʟᴇ sᴛʀᴇᴀᴍɪɴɢ ʙᴏᴛ ᴛʜᴀᴛ ɢᴇɴᴇʀᴀᴛᴇs ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs!</b>\n
<b>Sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴏʀ ᴍᴇᴅɪᴀ ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ.</b>\n
<b>💕 @{}</b>\n"""

    HELP_TEXT = """
<b>🔖 <u>Hᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ</u>:</b>\n
<b>• Aᴅᴅ ᴍᴇ ᴀs ᴀɴ ᴀᴅᴍɪɴ ᴏɴ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟs (ᴏᴘᴛɪᴏɴᴀʟ).</b>
<b>• Sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴅᴏᴄᴜᴍᴇɴᴛ, ᴠɪᴅᴇᴏ, ᴏʀ ᴀᴜᴅɪᴏ ғɪʟᴇ.</b>
<b>• I ᴡɪʟʟ ɪɴsᴛᴀɴᴛʟʏ ᴘʀᴏᴠɪᴅᴇ ᴀ ғᴀsᴛ sᴛʀᴇᴀᴍɪɴɢ & ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ!</b>\n
<b>🔞 <u>Wᴀʀɴɪɴɢ</u>: Aᴅᴜʟᴛ ᴄᴏɴᴛᴇɴᴛ ɪs sᴛʀɪᴄᴛʟʏ ᴘʀᴏʜɪʙɪᴛᴇᴅ.</b>\n
<i><b>💬 Rᴇᴘᴏʀᴛ ʙᴜɢs ᴛᴏ ᴛʜᴇ Dᴇᴠᴇʟᴏᴘᴇʀ</b></i>"""

    ABOUT_TEXT = """
<b>🤖 Mʏ Nᴀᴍᴇ : {}</b>\n
<b>📈 Vᴇʀsɪᴏɴ : {}</b>
<b>👨‍💻 Dᴇᴠᴇʟᴏᴘᴇʀ : FileStream Admin</b>\n
"""

    STREAM_TEXT = """
<i><u>✨ Yᴏᴜʀ Lɪɴᴋ ɪs Rᴇᴀᴅʏ!</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🖥 Wᴀᴛᴄʜ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""

    STREAM_TEXT_X = """
<i><u>✨ Yᴏᴜʀ Lɪɴᴋ ɪs Rᴇᴀᴅʏ!</u></i>\n
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ :</b> <b>{}</b>\n
<b>📦 Fɪʟᴇ ꜱɪᴢᴇ :</b> <code>{}</code>\n
<b>📥 Dᴏᴡɴʟᴏᴀᴅ :</b> <code>{}</code>\n
<b>🔗 Sʜᴀʀᴇ :</b> <code>{}</code>\n"""

    BAN_TEXT = "__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ғʀᴏᴍ ᴜsɪɴɢ ᴍᴇ.__\n\n**[Cᴏɴᴛᴀᴄᴛ Dᴇᴠᴇʟᴏᴘᴇʀ](tg://user?id={}) ᴛᴏ ᴀᴘᴘᴇᴀʟ.**"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close')
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ᴀʙᴏᴜᴛ', callback_data='about'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='home'),
            InlineKeyboardButton('ʜᴇʟᴘ', callback_data='help'),
            InlineKeyboardButton('ᴄʟᴏsᴇ', callback_data='close'),
        ],
            [InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
