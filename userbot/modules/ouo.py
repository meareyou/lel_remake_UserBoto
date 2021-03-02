import json
from time import sleep
import requests
from userbot import CMD_HELP
from userbot.events import register


import  @register(outgoing=True, pattern=r"^\.ouo ?(.*)")
async def _(event):
    url = event.pattern_match.group(1)
    if not url:
        await event.edit("Mau bypass apa")
        sleep(3)
        await event.edit("Hatiku 🤩")
    elif 'https://' not in url:
        await event.edit('Masukan url OuO')
        return
    else:# f"FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4"
         uro = 'https://akasakaidn.herokuapp.com/ouo/?url='
         p = requests.get(uro+url)
         jsno = p.json()
         json_result = jsno["result"]
         msg += f"`json_result`\n"
         msg += f"Congrats"
           await.event.edit(msg)


CMD_HELP.update({
    "ouo":
    "OuO Bypass"
    "\n > `.ouo <link>`"
})
