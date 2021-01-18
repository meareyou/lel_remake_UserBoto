import html
import requests
import asyncio
import html
from bs4 import BeautifulSoup as bs
import re
from userbot import CMD_HELP
from userbot.events import register

@register(outgoing=True, pattern=r"^\.neonime ?(.*)")
async def _(event):
    url = 'https://neonime.vip/episode/'
    ht_ = requests.get(url).text
    _bs = bs(ht_,"html.parser")
    bd_ = _bs.findAll('td',class_='bb')
    out = f"**New Episode**:\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+Subtitle\s+Indonesia\s+Season.\d+','',tt_)
            link = hh['href']
            out += f"- <a href='{link}'>{_tt}</a>"
            await event.edit(out,parse_mode='html')
            await event.delete()

CMD_HELP.update({
    "neonime":
        ".neonime\
        \nUsage: liat anime baru rilis dari neonime"
})
