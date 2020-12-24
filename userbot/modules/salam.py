from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.PP(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER} Mengucapkan**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


@register(outgoing=True, pattern='^.pp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER} Mengucapkan**")
    sleep(2)
    await typew.edit("`Assalamualaikum.....`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


@register(outgoing=True, pattern='^.LL(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam......`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


@register(outgoing=True, pattern='^.ll(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Astaghfirulloh Jawab Salam Dong...`")
    sleep(1)
    await typew.edit("`Waallaikumsalam.....`")
    sleep(30)
    await msg.delete()
# Owner @Si_Dian + @Crypto08


CMD_HELP.update({
    "salam":
    "`.pp/PP`\
\nUsage: Untuk Memberi salam.\
\n\n`.LL/.ll`\
\nUsage: Untuk Menjawab Salam."
})
