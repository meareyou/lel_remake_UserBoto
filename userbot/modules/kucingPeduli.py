from bs4 import BeautifulSoup as bs
import requests as re
from userbot.events import register
from userbot import CMD_HELP


@register(outgoing=True, pattern=r"^.kucingpeduli ?(.*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        await event.edit("Usage: .kucingpeduli <Hentai Name>")
        return
    att = []
    a = f"https://nekopoi.care/?s={s}"
    b = re.get(a).text
    c = bs(b, "html.parser")
    if c.find('div', attrs={'class': 'postsbody'}).find(
            'h2').text == "Tidak ada hasil":
        await event.edit("not found")
    else:
        r = f"Result:\n"
        d = c.find('div', class_="result").parent.find_all('li')
        for arr in d:
            a = arr.find('h2').text.strip()
            b = arr.find('h2').findNext('a').attrs['href']
            att.append({
                "title": a,
                "url": b,
            })
        for k, v in enumerate(att):
            t = v["title"]
            u = v["url"]
            r += f"<a href='{u}'>{t}</a>"
            await event.edit(r)

CMD_HELP.update({
    "kucingPeduli":
        ".kucingpeduli <query>\
        \nUsage: search di neko"
})
