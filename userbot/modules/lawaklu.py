from telethon import events

from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import bot, CMD_HELP

from userbot.events import register

@register(outgoing=True, pattern=r"^\.regisno(?: |$)(.*)")

async def renom(event):

   if event.fwd_from:

        return

    link = event.pattern_match.group(1)

    chat = "@telkomsel_official_bot"

    await event.edit("``Processing``")

try:

    response = conv.wait_event(

       events.NewMessage(incoming=True,from_users=266446332))

       await bot.send_message(chat, link)

       response = await response

       await conv.get_response()      

       await event.delete()

       await bot.send_message(event.chat_id, response.message)

         

CMD_HELP.update(

    {

        "Cek kuota":">`.renom` <masukin nomor lu tsel only>"        

        "\nUsage: register nomor ke tsel ntar dpt kode sms\n\n"

        ">`.recode` <masukin kode sms yg lu dpt>"

        "\nUsage: kirim kode buat register"

        ">`.cekuota` <cek kuota>"

        "\nUsage: cek kuota Telkomsel only"

    }

)
