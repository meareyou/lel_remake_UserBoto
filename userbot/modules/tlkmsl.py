from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern=r"^\.tlkmsl(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    chat = "@telkomsel_official_bot"
    now = f"cek kuota"
    conf = f"Ya"
    await event.edit("`Processing...`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=266446332))
            await bot.send_message(chat, now)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Please unblock the Bot `@telkomsel_official_bot`")
            return
        if response.text.startswith("Agar"):
            await event.edit("`Please cek bot and complete your identity`")
            return
        else:
        await bot.send_message(chat, conf)
        await conv.get_response()
        await event.edit(f"{response.message.message}")

CMD_HELP.update({
    "telkomsel":
    "`.tlkmsl`"
    "\nUsage: Cek Kuota."
})
