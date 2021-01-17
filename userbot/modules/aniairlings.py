"""
	Shows anime airing time in anilist
	Usage : .airling anime name
	By : lel_remake_UserBoto
"""
import requests
from userbot import CMD_HELP
from userbot.events import register


# time formatter from uniborg
def time_(milliseconds: int) -> str:
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


def _api(str_):
    query = '''
    query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        title {
          romaji
          native
        }
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        }
        coverImage {
           extraLarge
        }
        startDate{
            year
        }
          episodes
          bannerImage
      }
    }
    '''
    variables = {
        'search': str_,
        "asHtml": True
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(
        url,
        json={
            'query': query,
            'variables': variables})
    jsonD = response.json()
    return jsonD


@register(outgoing=True, pattern=r"^.airling ?(.*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        await event.edit("Usage: .airling <Anime Name>")
        return
    result = _api(query)
    error = result.get('errors')
    if error:
        err = f"*Anime* : `{error[0].get('message')}`"
        await event.edit(err)
        print(err)
        return
    caption = ""
    data = result['data']['Media']
    mid = data.get('id')
    romaji = data['title']['romaji']
    native = data['title']['native']
    episodes = data.get('episodes')
    coverImg = data.get('coverImage')['extraLarge']
    caption += f"**Name**: **{romaji}**(`{native}`)"
    caption += f"\n**ID**: `{mid}`"
    if data['nextAiringEpisode']:
        time = data['nextAiringEpisode']['timeUntilAiring'] * 1000
        time = time_(time)
        caption += f"\n**Episode**: `{data['nextAiringEpisode']['episode']}`"
        caption += f"\n**Airing in**: `{time}`"
        await event.delete()
        await event.client.send_file(
            event.chat_id,
            file=coverImg,
            caption=caption,
            reply_to=event,
        )
    else:
        caption += f"\n**Episode**: `{episodes}`"
        caption += f"\n**Status**: `N/A`"
        await event.delete()
        await event.client.send_file(
            event.chat_id,
            file=coverImg,
            caption=caption,
            reply_to=event,
        )
CMD_HELP.update({
    "aniairlings":
    ".airlings <Anime name>\
    \nUsage: shows anime airing"
})
