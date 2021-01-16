from datetime import datetime
import time
import json
import requests
import asyncio
from userbot import CMD_HELP
from userbot.events import register


def callApi(search_str):
    query = '''
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
    variables = {
        'search': search_str
    }
    response = requests.post(
        'https://graphql.anilist.co',
        json={
            'query': query,
            'variables': variables})
    return response.text


async def formatJson(data_str):
    msg = ''
    jsonData = jsonData.loads(data_str)
    res = list(jsonData.keys())
    if 'errors' in res:
        msg += f"**Error** : `{jsonData['errors'][0]['message']}`"
        return msg
        else:
            jsonData = jsonData['data']['media']
            if 'bannerImage' in jsonData.keys():
                image = jsonData['bannerImage']
                else:
                    msg = f"*Name*: *{jsonData['title']['romaji']}*(`{jsonData['title']['native']}`)\n*ID*: `{jsonData['id']}`[⁠ ⁠]({image})"
                    if 'nextAiringEpisode' in jsonData.keys():
                        time = jsonData['nextAiringEpisode']['timeUntilAiring']
                        msg += f"\n*Episode*: `{jsonData['nextAiringEpisode']['episode']}`\n*Airing In*: `{time}`"
                        else:
                            msg += f"\n*Episode*:{jsonData['episodes']}\n*Status*: `N/A`"
                            return msg


@register(outgoing=True, pattern=r"^\.airings ?(.*)")
async def ani_anime(event):
    if event.fwd_from:
        return
    message = await event.get_reply_message()
    search_query = event.pattern_match.group(1)
    if search_query:
        pass
    elif message:
        search_query = message.text
        else:
            await event.edit("Format: `.airings <anime name>`")
            return
        result = await callApi(search_query)
        msg = await formatJson(result)
        await event.edit(msg, link_preview=True)

CMD_HELP.update({
    "anime airing":
    ".airings <anime name >\
     \nUSAGE: Shows you the airing of the anime."
})
