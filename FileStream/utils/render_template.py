import aiohttp
import jinja2
import urllib.parse
from FileStream.config import Telegram, Server
from FileStream.utils.database import Database
from FileStream.utils.human_readable import humanbytes
db = Database(Telegram.DATABASE_URL, Telegram.SESSION_NAME)

async def render_page(db_id):
    file_data=await db.get_file(db_id)
    src = urllib.parse.urljoin(Server.URL, f'dl/{file_data["_id"]}')
    file_size = humanbytes(file_data['file_size'])
    file_name = file_data['file_name'].replace("_", " ")

    if str((file_data['mime_type']).split('/')[0].strip()) == 'video':
        template_file = "FileStream/template/play.html"
    else:
        template_file = "FileStream/template/dl.html"
        async with aiohttp.ClientSession() as s:
            async with s.get(src) as u:
                file_size = humanbytes(int(u.headers.get('Content-Length')))

    with open(template_file) as f:
        template = jinja2.Template(f.read())

    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size,
        mime_type=file_data.get('mime_type', 'video/mp4')
    )

async def render_playlist_page(playlist_id):
    playlist = await db.get_playlist(playlist_id)
    if not playlist:
        from FileStream.server.exceptions import FIleNotFound
        raise FIleNotFound

    # Fetch file data for all files in the playlist
    files_data = []
    for file_id in playlist['files']:
        try:
            file_data = await db.get_file(file_id)
            src = urllib.parse.urljoin(Server.URL, f'dl/{file_data["_id"]}')
            file_size = humanbytes(file_data['file_size'])
            file_name = file_data['file_name'].replace("_", " ")
            mime_type = file_data.get('mime_type', 'video/mp4')
            files_data.append({
                "id": str(file_data["_id"]),
                "name": file_name,
                "size": file_size,
                "url": src,
                "mime_type": mime_type
            })
        except Exception:
            continue
            
    with open("FileStream/template/playlist.html") as f:
        template = jinja2.Template(f.read())

    import json
    return template.render(
        playlist_title=playlist['title'],
        playlist_id=str(playlist['_id']),
        files=files_data,
        files_json=json.dumps(files_data)
    )
