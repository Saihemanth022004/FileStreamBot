from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram


class LANG(object):

    START_TEXT = """
<b>Hey {} 👋</b>

<b>Welcome to FileStream ⚡</b>
I can turn your Telegram files into clean, instant links for:
• <b>direct download ⬇️</b>
• <b>browser streaming ▶️</b>
• <b>quick sharing 🔗</b>

Send me any file and I will handle the rest 🚀

<b>Bot:</b> @{}"""

    HELP_TEXT = """
<b>How To Use 🧭</b>

<b>1.</b> Send a file in private chat 📩
<b>2.</b> Wait a few seconds while I process it ⏳
<b>3.</b> Tap buttons to stream, download, or share 🎬

<b>Extra:</b> add me as admin in a channel to generate links from channel posts.

<b>Support:</b> <a href="tg://user?id={}">contact the developer</a>
<b>Note:</b> prohibited or abusive content is not allowed."""

    ABOUT_TEXT = """
<b>About FileStream 🤖</b>

<b>Name:</b> {}
<b>Version:</b> {}
<b>What it does:</b> creates fast stream and download links for Telegram files
<b>Maintained by:</b> FileStream Admin"""

    STREAM_TEXT = """
<b>Your file is ready ✅</b>

<b>File:</b> <code>{}</code>
<b>Size:</b> <code>{}</code>

<b>Download link</b>
<code>{}</code>

<b>Watch link</b>
<code>{}</code>

<b>Share link</b>
<code>{}</code>"""

    STREAM_TEXT_X = """
<b>Your file is ready ✅</b>

<b>File:</b> <code>{}</code>
<b>Size:</b> <code>{}</code>

<b>Download link</b>
<code>{}</code>

<b>Watch link</b>
<code>{}</code>

<b>Share link</b>
<code>{}</code>"""

    BAN_TEXT = "<b>Access denied 🚫</b>\n\nYou are currently banned from using this bot.\nIf you believe this is a mistake, <a href=\"tg://user?id={}\">contact the developer</a>."
    FORCE_SUB_TEXT = """
<b>Join the updates channel to continue.</b>

After joining, send your command or file again."""
    FILES_TEXT = """
<b>Your Files</b>

<b>Total files:</b> {}"""
    FILE_DETAILS_TEXT = """
<b>File Details</b>

<b>Name:</b> <code>{}</code>
<b>Size:</b> <code>{}</code>
<b>Type:</b> <code>{}</code>
<b>Created:</b> <code>{}</code>"""
    DELETE_CONFIRM_TEXT = """
<b>Delete this file?</b>

This removes its saved link from the bot."""
    DELETE_SUCCESS_TEXT = "<b>File deleted successfully.</b>"
    INVALID_COMMAND_TEXT = "<b>Invalid command.</b>"
    FILE_NOT_FOUND_TEXT = "<b>File not found 🫠</b>"
    SOMETHING_WENT_WRONG = "<b>Something went wrong 😓</b>"
    PROCESSING_TEXT = "<b>Processing your file ⚙️</b>\nPlease wait a moment..."
    PING_TEXT = "<b>Checking bot response 🛰️</b>"
    PONG_TEXT = "<b>Bot is online ✅</b>\n<b>Latency:</b> <code>{} ms</code>"
    AUTH_DENIED_TEXT = "<b>Access restricted 🔒</b>\n\nYou are not authorized to use this bot."
    FORCE_SUB_ERROR_TEXT = "<b>Something went wrong 😓</b>\n\nPlease contact the developer or visit the updates channel."


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('How To Use', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about')
        ],
            [InlineKeyboardButton("Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')],
            [InlineKeyboardButton('Close', callback_data='close')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about')
        ],
            [InlineKeyboardButton("Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')],
            [InlineKeyboardButton('Close', callback_data='close')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('How To Use', callback_data='help')
        ],
            [InlineKeyboardButton("Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')],
            [InlineKeyboardButton('Close', callback_data='close')]
        ]
    )
