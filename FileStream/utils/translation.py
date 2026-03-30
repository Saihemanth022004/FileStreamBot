from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.config import Telegram


class LANG(object):

    START_TEXT = """
🚀 <b>/start</b>
👋 Welcome to <b>Sai FileStream Bot</b> ⚡️

Turn your Telegram files into:
• ⬇️ Direct download links
• ▶️ Instant browser streaming
• 🔗 Clean, shareable URLs

📂 Just send any file — I'll handle the rest.

⚡ Fast. Simple. Reliable.

🔗 Share with friends: @{}"""

    HELP_TEXT = """
🛠 <b>/help</b>
🧠 How to use <b>Sai FileStream Bot</b>:

1️⃣ Send any file (video, document, etc.)
2️⃣ Wait a few seconds ⏳
3️⃣ Get your instant link 🔗

You can:
• Download directly ⬇️
• Stream in browser ▶️
• Share anywhere 🔗

💡 Tip: Best for videos, PDFs, and large files"""

    ABOUT_TEXT = """
ℹ️ <b>/about</b>
📢 About <b>Sai FileStream Bot</b> ⚡️

This bot converts Telegram files into clean, usable links for streaming and sharing.

⚡ Built for speed
💡 Designed for simplicity
🚀 Created by Sai

Making file sharing effortless."""

    STREAM_TEXT = """
<b>Your file is ready ✅</b>

<b>File:</b> <code>{}</code>
<b>Size:</b> <code>{}</code>

<b>Download link</b>
<code>{}</code>

<b>Watch link</b>
<code>{}</code>

<b>Share link</b>
<code>{}</code>

<b>⚠️ Expiry:</b> This file link will expire automatically after <b>5 days</b>."""

    STREAM_TEXT_X = """
<b>Your file is ready ✅</b>

<b>File:</b> <code>{}</code>
<b>Size:</b> <code>{}</code>

<b>Download link</b>
<code>{}</code>

<b>Watch link</b>
<code>{}</code>

<b>Share link</b>
<code>{}</code>

<b>⚠️ Expiry:</b> This file link will expire automatically after <b>5 days</b>."""

    BAN_TEXT = "<b>Access denied 🚫</b>\n\nYou are currently banned from using this bot.\nIf you believe this is a mistake, <a href=\"tg://user?id={}\">contact the developer</a>."
    FORCE_SUB_TEXT = """
<b>Join the updates channel to continue.</b>

After joining, send your command or file again."""
    FILES_TEXT = """
📂 <b>Your Recent Files:</b>

👇 Select a file to view options."""
    FILES_TEXT_EMPTY = """
📂 <b>No files yet.</b>

Send your first file and I'll convert it instantly ⚡"""
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
