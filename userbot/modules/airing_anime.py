import html
import json
import textwrap
from urllib.parse import quote as urlencode
import aiohttp
import bs4
import jikanpy
import requests
from jikanpy import Jikan
from jikanpy.exceptions import APIException
from telethon.errors.rpcerrorlist import FilePartsInvalidError
from telethon.tl.types import (DocumentAttributeAnimated,                               DocumentAttributeFilename, MessageMediaDocument)

from telethon.utils import is_image, is_video
from userbot import CMD_HELP
from userbot.events import register

jikan = Jikan()
   
def t(milliseconds: int) -> str:
    """Inputs time in milliseconds, to get beautified time,
    as string"""
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + " Days, ") if days else "") + \
        ((str(hours) + " Hours, ") if hours else "") + \
        ((str(minutes) + " Minutes, ") if minutes else "") + \
        ((str(seconds) + " Seconds, ") if seconds else "") + \
        ((str(milliseconds) + " ms, ") if milliseconds else "")
    return tmp[:-2]
    
    
 airing_query = '''
    query ($id: Int,$search: String) { 
      Media (id: $id, type: ANIME,search: $search) { 
        id
        siteUrl
        bannerImage 
        episodes
        title {
          romaji
          english
          native
        }
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        } 
      }
    }
    '''
    
url = 'https://graphql.anilist.co'
  
@register(outgoing=True, pattern=r"^\.airings ?(.*)")
async def anime_airing(event):
  query = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    await event.edit("`Searching Anime...`")
if query:
  pass
elif reply:
  query = reply.text
  else
  await event.edit("Tell anime name: .airings <anime name>")
  await event.delete()
 return
try:
  variables = {'search': query}
  response = requests.post(
        url, json={
            'query': airing_query,
            'variables': variables
        }).json()['data']['Media']
    image = response.get('bannerImage', None)
    msg = f"*Name*: *{response['title']['romaji']}*(`{response['title']['native']}`)\n*ID*: `{response['id']}`[⁠ ⁠]({image})"
   if response['nextAiringEpisode']:
     msg = f"*Name*: *{response['title']['romaji']}*(`{response['title']['native']}`)\n*ID*: `{response['id']}`[⁠ ⁠]({image})"
    if response['nextAiringEpisode']:
        time = response['nextAiringEpisode']['timeUntilAiring'] * 1000
        time = t(time)
        msg += f"\n*Episode*: `{response['nextAiringEpisode']['episode']}`\n*Airing In*: `{time}`"
    else:
        msg += f"\n*Episode*:{response['episodes']}\n*Status*: `N/A`"
     await event.delete()
    await event.client.send_file(
        event.chat_id,
        file=image,
        meg=replace_text(msg))
