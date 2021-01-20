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

CMD_HELP.update({
    "neonime":
        "Download anime Dari Neonime\
        \n\n.neonime\"
        "\nUsage: liat anime baru rilis dari neonime\"
})
