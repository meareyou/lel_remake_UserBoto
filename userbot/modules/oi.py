from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.oi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`GW GANTENG..`")
    sleep(3)
    await typew.edit("`GW GANTENG BANGET`")
    sleep(1)
    await typew.edit("`GW GANTENG BANGET NYA KEBANGETAN`")
    # original by @localheart edited by @Crypto08


@register(outgoing=True, pattern='^.io(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`GW GANTENG BANGET ...`")
    sleep(3)
    await typew.edit("`GW GANTENG BANGET ANJIM`")
    sleep(1)
    await typew.edit("`GW GANTENG LEBIHIN LO`")
# line 14


@register(outgoing=True, pattern='^.ll(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Di tolak buat ngeuue ...`")
    sleep(3)
    await typew.edit("`Tapi Gua nggak nyesel ❤️😧`")
    sleep(1)
    await typew.edit("`I love memki`")
# line 14
