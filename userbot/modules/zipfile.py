""" command: .compress """
#

from telethon import events
import asyncio
import zipfile
from pySmartDL import SmartDL
from userbot.events import register
from datetime import date
import time
import os
from userbot import TEMP_DOWNLOAD_DIRECTORY, ZIP_DOWNLOAD_DIRECTORY, bot
from userbot import CMD_HELP
# from uniborg.util import admin_cmd, humanbytes, progress, time_formatter
from userbot.util import admin_cmd, humanbytes, progress, time_formatter

#  @borg.on(admin_cmd("compress"))
@register(outgoing=True, pattern=r"^.compress(?: |$)(.*)")
async def _(event):
    #Prevent Channel Bug to use update
    if event.is_channel and not event.is_group:
        await event.edit("`compress Command isn't permitted on channels`")
        return
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("Reply to a file to compress it.")
        return
    mone = await event.edit("Processing ...")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                )
            )
            directory_name = downloaded_file_name
            await event.edit(downloaded_file_name)
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
    zipfile.ZipFile(directory_name + '.zip', 'w', zipfile.ZIP_DEFLATED).write(directory_name)
    await bot.send_file(
        event.chat_id,
        directory_name + ".zip",
        caption="`File zipped!`",
        force_document=True,
        allow_cache=False,
        reply_to=event.message.id,
    )
    await event.edit("DONE!!!")
    await asyncio.sleep(7)
    await event.delete()


@register(outgoing=True, pattern=r"^.addzip(?: |$)(.*)")
async def addzip(add):
    """ Add file to zip list """
    #Prevent Channel Bug to use update
    if add.is_channel and not add.is_group:
        await event.edit("`compress Command isn't permitted on channels`")
        return
    if add.fwd_from:
        return
    if not add.is_reply:
        await add.edit("Reply to a file to compress it.")
        return
    directroy_zip = zip
    mone = await add.edit("Processing ...")
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        os.makedirs(ZIP_DOWNLOAD_DIRECTORY)
    if add.reply_to_msg_id:
        reply_message = await add.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                ZIP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "trying to download")
                )
            )
            directory_name = downloaded_file_name
            await add.edit(downloaded_file_name)
        except Exception as e:  # pylint:disable=C0103,W0703
            await mone.edit(str(e))
            return


@register(outgoing=True, pattern=r"^.upzip(?: |$)(.*)")
async def upload_zip(up):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await up.edit(f"`Files not found`")
        return
    input_str = up.pattern_match.group(1)
    curdate = today.strftime("%m%d%y")
    if input_str:
        title = str(input_str)
    else:
        title = "zipfile" + f"{curdate}"
    zipf = zipfile.ZipFile(title + '.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir(ZIP_DOWNLOAD_DIRECTORY, zipf)
    zipf.close()
    await bot.send_file(
        up.chat_id,
        title + ".zip",
        caption="Zipped By EyePatch",
        force_document=True,
        allow_cache=False,
        reply_to=event.message.id,
    )
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))


CMD_HELP.update({
        "zipfile":
        ">`.compress` [optional: <reply to file >]\
            \nUsage: make files to zip."
        "\n>`.addzip` <reply to file >\
            \nUsage: add files to zip list."
        "\n>`.upzip` [optional: <zip title>]\
            \nUsage: upload zip list."
})
