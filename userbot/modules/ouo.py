import json
import urllib.request
from telethon import event
from userbot import bot
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.ouo ?(.*)")
async def _(event):  # FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
    uro = event.pattern_match.group(1)
    if not url:
        await event.edit("Lah yg mau di bypass mana"")
    elif 'https://' not in url:
        await event.edit('Masukan url')
        return
    else:
    	url = "https://akasakaid.herokuapp.com/ouo/?url="
data = urllib.request.urlopen(url + uro).read().decode()
obj = json.loads(data)
# FKTnK3aKtFvMSUiWLZrTuAp4g93VSjbXcR5zGmqWAijuAuYgR2ACP8WNot2ZyTRVECks1uV5WWW7muWz5SZkY2P8YbWW6AYLUFTsmFU1oW9Y2GP4
print('Link : ' + "(Duar)[" + obj['result'] + "]")

CMD_HELP.update({
                 "ouo":
                 "\n >`.ouo links`"
                 "\n  Usage: bypass __ouo.io__."



                # t.me/crypto08
                 # special thanks @akasakaid
