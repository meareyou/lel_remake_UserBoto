import html
from requests import Session
import asyncio
import html
from bs4 import BeautifulSoup as bs
from userbot import CMD_HELP
from userbot.events import register

r = Session()
ua = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'}

@register(outgoing=True, pattern=r"^\.neko ?(.*)")
async def _search(event):
    uri = event.pattern_match.group(1)
    if not uri:
        await event.edit("Masukan keyword pencarian")
        return
    else:
        url = f"https://nekopoi.care/?s={qu}"
        _a = r.get(url,headers=ua).text
        _b = bs(_a,'html.parser')
        o_ = f"**Hasil search Dari kucing peduli**\n\n"
       if _b.find('div',attrs={'class':'postsbody'}).find('h2').text == "Tidak ada hasil":
          await event.edit('tidak ada hasil')
       else:
           _c = _b.find('div',attrs={'class':'result'}).find('ul').findAll('li')
           for _d in _c:
               _e = _d.find('h2').find('a').text
               o_ += f"* {_e}"
               await event.edit(o_)
        
CMD_HELP.update({
    "kucingpeduli":
    ".nekop <nama>\
    \nUsage: cari anime di kucingpoi.peduli"
})
