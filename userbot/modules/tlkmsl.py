import os
from time import sleep
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern=r"^\.tlkmsl(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
        chat = "@telkomsel_official_bot"
    now = f"/now"
    await event.edit("`Processing...`")
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(now)
            response = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("`Please unblock the Bot `@telkomsel_official_bot`")
            return
        if response.text.startswith("Agar"):
            await event.edit("`Please cek bot and complete your identity`")
            return
        else:
           await event.edit(f"{response.message.message}")