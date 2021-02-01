from userbot import CMD_HELP
from userbot.events import register
import requests 

@register(outgoing=True, pattern=r"^\.kucing ?(.*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        await event.edit("Usage: <query>")
    else:
        await event.edit("Tungguuuu....")
        url = "https://nekosearch.frissst.repl.co/search/"
        req = requests.get(url + query)
        jsons = req.json()
        msg = f"<b>Hasil: {query}</b>\n\n"
        if not jsons["success"]:
            await event.edit("404 Not found")
        else:
            m_result = jsons["result"]
            for result in m_result:
                m_title = result["title"]
                m_video_url = result["url"]
                msg += f"~ <a href='{m_video_url}'>{m_title}</a>\n"
                await event.edit(msg, parse_mode="html")

CMD_HELP.update({
    "nekocare":
        "Nekopoi search:\
          \n> Usage: .kucing <query>\
           \n Cari jav/hen di nekopoi"
})
