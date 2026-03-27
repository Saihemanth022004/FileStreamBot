from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram


class LANG(object):

    START_TEXT = """
<b>Welcome, {}.</b>

I can turn your Telegram files into:
• direct download links
• browser stream links
• quick shareable access links

Send any file to get started.

<b>Bot:</b> @{}"""

    HELP_TEXT = """
<b>How to use this bot</b>

1. Send a file in private chat.
2. Wait a moment while I process it.
3. Use the buttons to stream, download, or share it.

<b>Optional:</b> add the bot as an admin in your channel to generate links from channel posts too.

<b>Note:</b> prohibited or abusive content is not allowed.
<b>Support:</b> contact <a href="tg://user?id={}">the developer</a> if you run into issues."""

    ABOUT_TEXT = """
<b>About This Bot</b>

<b>Name:</b> {}
<b>Version:</b> {}
<b>Purpose:</b> create fast stream and download links for Telegram files
<b>Maintained by:</b> FileStream Admin"""

    STREAM_TEXT = """
<b>Your file is ready.</b>

<b>File:</b> {}
<b>Size:</b> <code>{}</code>

<b>Download:</b>
<code>{}</code>

<b>Watch:</b>
<code>{}</code>

<b>Share:</b>
<code>{}</code>"""

    STREAM_TEXT_X = """
<b>Your file is ready.</b>

<b>File:</b> {}
<b>Size:</b> <code>{}</code>

<b>Download:</b>
<code>{}</code>

<b>Share:</b>
<code>{}</code>"""

    BAN_TEXT = "<b>Access denied.</b>\n\nYou are banned from using this bot.\nContact <a href=\"tg://user?id={}\">the developer</a> if you want to appeal."
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

This will remove its saved link from the bot."""
    DELETE_SUCCESS_TEXT = "<b>File deleted successfully.</b>"
    INVALID_COMMAND_TEXT = "<b>Invalid command.</b>"
    FILE_NOT_FOUND_TEXT = "<b>File not found.</b>"
    SOMETHING_WENT_WRONG = "<b>Something went wrong.</b>"
    PROCESSING_TEXT = "<b>Processing your file...</b>"
    PING_TEXT = "<b>Checking bot response...</b>"
    PONG_TEXT = "<b>Pong.</b>\n<b>Latency:</b> <code>{} ms</code>"


class BUTTON(object):
    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close')
        ],
            [InlineKeyboardButton("Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('About', callback_data='about'),
            InlineKeyboardButton('Close', callback_data='close'),
        ],
            [InlineKeyboardButton("Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('Home', callback_data='home'),
            InlineKeyboardButton('Help', callback_data='help'),
            InlineKeyboardButton('Close', callback_data='close'),
        ],
            [InlineKeyboardButton("Updates Channel", url=f'https://t.me/{Telegram.UPDATES_CHANNEL}')]
        ]
    )
