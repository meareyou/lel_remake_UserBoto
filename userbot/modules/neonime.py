import requests
from bs4 import BeautifulSoup as bs
import re
from userbot import CMD_HELP
from userbot.events import register

# blom kelar heduh pusing


@register(outgoing=True, pattern=r"^\.neonime ?(.*)")
async def _neonime(event):
    await event.edit('tunggu bentar...')
    url = 'https://neonime.vip/episode/'
    ht_ = requests.get(url).text
    _bs = bs(ht_, "html.parser")
    bd_ = _bs.findAll('td', class_='bb')
    out = "<b>New Episode:</b>\n\n"
    for kntl_ in bd_:
        _lucu = kntl_.find('a')
        if not _lucu:
            _lucu = 'none'
        else:
            tt_ = _lucu.get_text()
            _tt = re.sub(r'\s+Subtitle\s+Indonesia\s+Season.\d+', '', tt_)
            link = _lucu['href']
            out += f"• <a href='{link}'>{_tt}</a>\n"
            if len(out) > 1000:
                break
            await event.edit(out, parse_mode="html")


@register(outgoing=True, pattern=r"^\.neolink ?(.*)")
async def _neolink(event):
    uri = event.pattern_match.group(1)
    if not uri:
        await event.edit("Masukan url episode, liat .help neonime")
    elif 'https://' not in uri:
        await event.edit('Masukan url')
        return
    else:
        uri = uri
        req = requests.get(uri).text
        sho = bs(req, 'html.parser')
        eps = sho.findAll('div', class_='sbox')
        tm_ = _ase.find_all('li')
        tk = f"{tm_}"
        tt = re.sub(r"</li>","\n</li>\n",tk)
        xs = f"{tt}"
        await event.edit(xs, parse_mode='html')

CMD_HELP.update({
    "neonime":
        "Download anime Dari Neonime\
        \n\n.neonime\
        \nUsage: liat anime baru rilis dari neonime\
        \n\n.neolink <Url link>\
        \nUsage: cari download link\
        \n\nCopy Url link dari .neonime"
})
