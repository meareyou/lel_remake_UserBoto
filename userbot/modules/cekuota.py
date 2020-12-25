from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^\.cekuota(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    in_ = event.pattern_match.group(1)
    c_ = "@telkomsel_official_bot"
    await event.edit("```Tunggu bntr```")
    async with bot.conversation(c_) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(
                    incoming=True,
                    from_users=424466890))
            await bot.send_message(c_, in_)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @nHentaiBot and try again```")
            return
        if response.text.startswith("**Untuk pelayanan maksimal, tolong tulis nomor Telkomsel Kamu ya (Contoh: 0811000000)**"):
            await event.edit("```Nomor belom terdaftar daftar dlu @telkomsel_official_bot```")
        elif response.text.startswith("**Agar bisa Veronika proses, tolong tuliskan nomor Telkomsel Kamu :)**"):
            await event.edit("```Nomor belom terdaftar daftar dlu @telkomsel_official_bot```")
        elif response.text.startswith("**Sebelum Veronika proses, apa Kamu mau melanjutkan permintaan tersebut dengan nomor**"):
            await event.delete()
            await bot.send_message(c_, "Ya")
            await bot.send_message(event.chat_id, response.message)

CMD_HELP.update({
    "cekuota":
    "`.cekuota` <cek kuota> \
\nUsage: Cek kuota telkomsel dari @telkomsel_official_bot \n"})