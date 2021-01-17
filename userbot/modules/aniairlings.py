import json
import json
import requests
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
        description (asHtml: false)
        startDate{
            year
          }
          episodes
          chapters
          volumes
          season
          type
          format
          status
          duration
          averageScore
          genres
          bannerImage
      }
    }
    '''
    variables = {
        'search': str_
    }
    url = 'https://graphql.anilist.co'
    response = requests.post(
        url,
        json={
            'query': query,
            'variables': variables})
    return response.text


def jsonResult(resp):
    msg = ""
    mData = json.loads(resp)
    err = list(mData.keys())
    if "errors" in err:
        msg += f"**Anime** : `{mData['errors'][0]['message']}`"
        return msg
    else:
        mResult = mData['data']['Media']
        msg += mResult['bannerImage']
        msg += f"*Name*: *{mResult['title']['romaji']}*(`{mResult['title']['native']}`)\n*ID*: `{mResult['id']}`"
        if mResult['nextAiringEpisode']:
            time = mResult['nextAiringEpisode']['timeUntilAiring'] * 1000
            time = t(time)
            msg += f"\n*Episode*: `{mResult['nextAiringEpisode']['episode']}`\n*Airing In*: `{time}`"
        else:
            return msg


@register(outgoing=True, pattern=r"^.airling ?(.*)")
async def _(event):
    r_ = await event.get_reply_message()
    q_ = event.pattern_match.group(1)
    if q_:
        pass
    elif r_:
        q_ = r_.text
    else:
        await event.edit("Usage: .airlings <Anime Name>")
        return
    mJson = _api(q_)
    mData = jsonResult(mJson)
    await event.edit(mData, link_preview=True)

CMD_HELP.update({
    "Anime Airing":
        "Usage: .airling <Anime Name>\
        \nShows you the airing of the anime"
})
