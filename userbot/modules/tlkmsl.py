from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
from userbot.events import register


@register(outgoing=True, pattern=r"^\.tlkmsl")
async def _(event):
    if event.fwd_from:
        return
    chat = "@telkomsel_official_bot"
    now = "cek kuota"
    await event.edit("Processing..")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=266446332))
            await bot.send_message(chat, now)
            response = await response
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.reply("unblock me (@telkomsel_official_bot) and try again")
            return
        if response.text.startswith("Untuk"):
            await event.edit("Please cek bot and complete your identity")
        else:
            await event.delete()
            await bot.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, response.message)
