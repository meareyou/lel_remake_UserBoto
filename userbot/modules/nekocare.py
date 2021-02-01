import asyncio
from pyppeteer import launch
from bs4 import BeautifulSoup
from userbot import CMD_HELP
from userbot.events import register


async def search(anime: str):
    browser = await launch(args=["--no-sandbox"], handleSIGINT=False,
                           handleSIGTERM=False,
                           handleSIGHUP=False)
    page = await browser.newPage()
    await page.goto(f"https://nekopoi.care/?s={anime}&post_type=anime")
    html = await page.evaluate('''() => {
    return document.body.innerHTML;
  }''')
    await page.close()
    await browser.close()
    return html


def s(anime: str, loop):
    asyncio.set_event_loop(loop)
    task = loop.create_task(search(anime))
    val = loop.run_until_complete(task)
    loop.close()
    return val


def _search(anime: str):
    try:
        loop = asyncio.new_event_loop()
        html = s(anime, loop)
        soup = BeautifulSoup(html, "html5lib")
        all_contents = soup.find('div', class_="result").parent.find_all('li')
        contents = []
        for content in all_contents:
            title = content.find('h2').text.strip()
            videoURL = content.find('h2').findNext('a').attrs['href']
            contents.append({
                "title": title,
                "url": videoURL,
            })
        return contents
    except BaseException:
        return None


@register(outgoing=True, pattern=r"^\.kucing ?(.*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        await event.edit("Null")
    else:
        result_anime = _search(query)
        msg = f"<b>Result: {query}</b>\n\n"
        if result_anime is None:
            await event.edit("404 not found")
        else:
            for k, v in enumerate(result_anime):
                url = v["url"]
                title = v["title"]
                msg += f"> <a href='{url}'>{title}</a>"
                await event.edit(msg, parse_mode="html")

CMD_HELP.update({
    "nekocare":
        "> Usage: .kucing <query>\
        \nCari jav/hen di nekopoi"
})
