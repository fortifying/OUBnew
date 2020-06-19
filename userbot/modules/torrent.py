# Copyright (C) 2020 GengKapak and AbggaR96s.
# All rights reserved.

import requests
import json
import asyncio
import os
from userbot import CMD_HELP, TEMP_DOWNLOAD_DIRECTORY
from userbot.events import register

@register(outgoing=True, pattern="^\.ts (.*)")
async def gengkapak(e):
    await e.edit("`Please wait, fetching results...`")
    query = e.text.split(" ", 1)[1]
    response = requests.get(f"https://sjprojectsapi.herokuapp.com/torrent/?query={query}")
    ts = json.loads(response.text)
    if not ts == response.json():
        await e.edit("**Some error occured**\n`Try Again Later`")
        return
    listdata = ""
    run = 0
    while True:
        try:
            run += 1
            r1 = ts[run]
            list1 = "<-----{}----->\nName: {}\nSeeders: {}\nSize: {}\nAge: {}\n<--Magnet Below-->\n{}\n\n\n".format(run, r1['name'], r1['seeder'], r1['size'], r1['age'], r1['magnet'])
            listdata = listdata + list1
        except:
            break

    tsfileloc = f"{TEMP_DOWNLOAD_DIRECTORY}/torrent_search.txt"
    caption = f"Here are the results for the query: {query}"
    with open(tsfileloc, "w+", encoding="utf8") as out_file:
        out_file.write(str(listdata))
    await e.client.send_file(
        e.chat_id,
        tsfileloc,
        caption=caption,
        force_document=False)
    os.remove(tsfileloc)
    await e.delete()


CMD_HELP.update({
    "torrent":
    ">`.ts` **Query**"
    "\nUsage: Search for torrent query and display results."
})
