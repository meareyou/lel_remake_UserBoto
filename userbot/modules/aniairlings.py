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
# Don't do anything
# f"FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4"


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


"""Jadwal rilis anime"""


def getList():
    list_ = []
    html = requests.get("https://otakudesu.tv/jadwal-rilis/")
    soup = bs(html.text, "html5lib")
    base = soup.find("div", class_="kgjdwl321")
    for daftar in base.find_all("div", class_="kglist321"):
        list_.append(daftar)
    return {"html": list_}


def getData(query):
    list_hari = []
    list_anime = []
    r = getList()["html"]
    for k, v in enumerate(r[query].find_all("li")):
        list_anime.append(v.find("a").get_text())
    for p, o in enumerate(r[query].find_all("h2")):
        list_hari.append(o.get_text())
    return {
        "hari": list_hari,
        "anime": list_anime
    }


@register(outgoing=True, pattern=r"^.airling ?(.*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        await event.edit("Usage: .airling <Anime Name>")
        return
    result = _api(query)
    error = result.get('errors')
    if error:
        err = f"**Anime** : `{error[0].get('message')}`"
        await event.edit(err)
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


@register(outgoing=True, pattern=r"^\.anirilis ?(.*)")
async def getResult(event):
    query = event.pattern_match.group(1).lower()
    if not query:
        await event.edit("**Usage**: `.anirilis` <Senin/Selasa>")
    else:
        await event.edit("Loading...")
        m_query = 0
        tbl_hari = [
            "senin",
            "selasa",
            "rabu",
            "kamis",
            "jumat",
            "sabtu",
            "minggu"]
        msg = "Jadwal Rilis Hari "
        if query == tbl_hari[0]:
            m_query = 0
        if query == tbl_hari[1]:
            m_query = 1
        if query == tbl_hari[2]:
            m_query = 2
        if query == tbl_hari[3]:
            m_query = 3
        if query == tbl_hari[4]:
            m_query = 4
        if query == tbl_hari[5]:
            m_query = 5
        if query == tbl_hari[6]:
            m_query = 6
        an_data = getData(m_query)["hari"]
        ar_data = getData(m_query)["anime"]
        for an_otr in an_data:
            msg += f"**{an_otr}**:\n"
        for an_ott in ar_data:
            msg += f" ~ `{an_ott}`\n"
        msg += f"\n**Note**: `Jadwal bisa berubah sewaktu-waktu`"
        await event.edit(msg)

# f"FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4"
CMD_HELP.update({
    "aniairlings":
    "`.airlings` <Anime name>\
    \n**Usage**: `shows anime airing`"
})
