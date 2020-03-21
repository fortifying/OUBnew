# ported to OUB by fortifying
from telethon import events
from userbot import CMD_HELP
from userbot.events import register

PRINTABLE_ASCII = range(0x21, 0x7f)


def aesthetify(string):
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)

@register(outgoing=True, pattern="^.ae(?: |$)(.*)")
#@register(events.NewMessage(pattern="^.ae(?: |$)(.*)', outgoing=True))
response = conv.wait_event(events.MessageEdited(outgoing=True, pattern="^.ae(?: |$)(.*)")
async def aes(event):
    text = event.pattern_match.group(1)
    text = "".join(aesthetify(text))
    await event.edit(text=text, parse_mode=None, link_preview=False)
    raise events.StopPropagation
    
    CMD_HELP.update({
        "aes": ".ae for aesthetic\
        \nUsage: Gatau buat apa anjjg.\"
    })

