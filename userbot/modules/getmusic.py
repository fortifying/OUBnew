# AnggaR96s
 
from telethon import events
import subprocess, instantmusic
from telethon.errors import MessageEmptyError, MessageTooLongError, MessageNotModifiedError
import io
import asyncio
import time
from userbot.events import register
from userbot import CMD_HELP
import glob
import os
 
os.system("rm -rf *.mp3")
 
 
def bruh(name):
    os.system("instantmusic -q -s "+name)
 
@register(outgoing=True, pattern=r"^.song (.*)")
async def _(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)
    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit("`Ok finding the song..`")
    bruh(str(cmd))
    l = glob.glob("*.mp3")
    loa = l[0]
    await event.edit("`Sending song..`")
    await event.client.send_file(
                event.chat_id,
                loa,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    os.system("rm -rf *.mp3")
    subprocess.check_output("rm -rf *.mp3",shell=True)
    await event.delete()
 
CMD_HELP.update({
    "song":
        ">`.song` **atrist title**"
        "\nUsage: Finding and uploading song."
})
 