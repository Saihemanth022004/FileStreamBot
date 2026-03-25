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

    page_link = urllib.parse.urljoin(Server.URL, f'watch/{file_data["_id"]}')
    poster_url = urllib.parse.urljoin(Server.URL, f'thumb/{file_data["_id"]}') if file_data.get('thumb_file_id') else urllib.parse.urljoin(Server.URL, 'logo.png')

    return template.render(
        file_name=file_name,
        file_url=src,
        file_size=file_size,
        mime_type=file_data.get('mime_type', 'video/mp4'),
        page_link=page_link,
        poster_url=poster_url
    )


