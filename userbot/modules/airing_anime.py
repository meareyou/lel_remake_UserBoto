import requests
import asyncio
from userbot import CMD_HELP
from userbot.events import register

# time formatter from uniborg


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


@register(outgoing=True, pattern=r"^\.airlings ?(.*)")
async def anime(event):
    query = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    if query:
        pass
    elif reply:
        query = reply.text
    else:
        await event.edit("`usage: .airlings <anime name> `")
        await asyncio.sleep(6)
        await event.delete()
        return
        variables = {'search': query}
        response = requests.post(
            url, json={
                'query': airing_query,
                'variables': variables
            }).json()['data']['Media']
        image = response.get('bannerImage', None)
        title_r = response['title']['romaji']
        title_n = response['title']['native']
        mId = response['id']
        msg = f"*Name*: *{title_r}*(`{title_n}`)\n*ID*: `{mId}`[⁠ ⁠]({image}"
        if response['nextAiringEpisode']:
            time = response['nextAiringEpisode']['timeUntilAiring'] * 1000
            times = t(time)
            eps = response['nextAiringEpisode']['episode']
            msg += f"\n*Episode*: `{eps}`\n*Airing In*: `{times}`"
        else:
            msg += f"\n*Episode*:{response['nextAiringEpisode']['episode']}\n*Status*: `N/A`"
            await event.edit(msg, parse_mode=ParseMode.MARKDOWN)

            CMD_HELP.update({
                "anime airing":
                ".airlings <anime name >\
     \nUSAGE: Shows you the airing of the anime."
            })
