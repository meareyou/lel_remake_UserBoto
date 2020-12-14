from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot.events import register
from userbot import bot, CMD_HELP


@register(outgoing=True, pattern=r"^\.gid(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("`Reply pesannya Ajg!!`")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Reply pesannya tolol!!```")
        return
    chat = "@getidsbot"
    reply_message.sender
    if reply_message.sender.bot:
        await event.edit("`Ngentood!!`")
        return
    await event.edit("`JADI CRACKER SEDANG BERJALAN.....`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=186675376))
            await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("`Bunuh @getidsbot dulu bos, biar botnya bisa jalan -_-`")
            return
        if response.text.startswith("Forward"):
            await event.edit("`Profil Buriq Tidak Punya ID...`")
        else:
            await event.edit(f"{response.message.message}")


CMD_HELP.update({
    "get_uid":
    "`.gid`"
    "\nUsage: Reply in message to get user ID."
})
