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


query = '''
    query ($id: Int,$search: String) {
      Media (id: $id, type: ANIME,search: $search) {
        id
        title {
          romaji
          native
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
        nextAiringEpisode {
           airingAt
           timeUntilAiring
           episode
        }
      }
    }
    '''


@register(outgoing=True, pattern=r"^.airlings ?(.*)")
async def _(event):
    q_ = event.pattern_match.group(1)
    await event.get_reply_message()
    if not q_:
        await event.edit('Usage: airlings <anime name>')
        await event.delete()
        return
    url = "https://graphql.anilist.co"
    vrb = {"search": q_}
    res = requests.post(url, json={
        "query": query,
        "variables": vrb
    }).json()["data"]["media"]

    res.get("bannerImage", None)
    res["title"]["romaji"]
    res["title"]["native"]
    res["id"]
    msg = f"*Name: *{t_r}*(`{t_n`})*ID: `{i_d}`[ ] ({image})*"
    await event.edit(msg)

CMD_HELP.update({
    "airlings":
        ".airlings <Anime name>\
        \nUSAGE: Show anime airing in time"
})
