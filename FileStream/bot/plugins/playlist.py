from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from FileStream.bot import FileStream
from FileStream.utils.database import Database
from FileStream.utils.file_properties import get_file_info
from FileStream.config import Telegram, Server

db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

@FileStream.on_message(filters.command("create_playlist") & filters.private)
async def create_playlist_handler(bot: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide a name.\nUsage: `/create_playlist My Show`")
    
    title = " ".join(message.command[1:])
    await db.create_playlist(message.from_user.id, title)
    await message.reply_text(f"✅ Playlist **{title}** created successfully!\n\nTo add videos, reply to any video you send me with `/add {title}`")

@FileStream.on_message(filters.command("add") & filters.private)
async def add_to_playlist_handler(bot: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.media:
        return await message.reply_text("Please reply to a video or file to add it.")
    if len(message.command) < 2:
        return await message.reply_text("Please provide the playlist name.\nUsage: `/add <name>`")

    title = " ".join(message.command[1:])
    
    # Get the file ID from the replied media
    file_info = get_file_info(message.reply_to_message)
    if not file_info:
        return await message.reply_text("This media is not supported.")
        
    inserted_id = await db.add_file(file_info)
    
    success = await db.add_file_to_playlist(message.from_user.id, title, inserted_id)
    if success:
        await message.reply_text(f"✅ Video perfectly added to **{title}**!")
    else:
        await message.reply_text(f"❌ Playlist **{title}** not found. Create it using `/create_playlist {title}` first.")

@FileStream.on_message(filters.command("my_playlists") & filters.private)
async def my_playlists_handler(bot: Client, message: Message):
    playlists = await db.get_my_playlists(message.from_user.id)
    if not playlists:
        return await message.reply_text("You don't have any playlists yet. Start by typing `/create_playlist`")
    
    text = "📁 **Your Playlists:**\n\n"
    for p in playlists:
        text += f"▪️ **{p['title']}** ({len(p['files'])} videos) - `/get_playlist {p['title']}`\n"
        
    await message.reply_text(text)

@FileStream.on_message(filters.command("get_playlist") & filters.private)
async def get_playlist_handler(bot: Client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("Please provide a name. Usage: `/get_playlist <name>`")
    
    title = " ".join(message.command[1:])
    playlists = await db.get_my_playlists(message.from_user.id)
    target_playlist = next((p for p in playlists if p['title'].lower() == title.lower()), None)
    
    if not target_playlist:
        return await message.reply_text(f"❌ Playlist **{title}** not found.")
        
    playlist_link = f"{Server.URL}playlist/{str(target_playlist['_id'])}"
    
    reply_markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("📺 Watch Playlist", url=playlist_link)]
    ])
    
    await message.reply_text(
        text=f"📺 **Playlist:** {target_playlist['title']}\n🍿 **Total Videos:** {len(target_playlist['files'])}\n\n🔗 {playlist_link}",
        reply_markup=reply_markup,
        disable_web_page_preview=True
    )
