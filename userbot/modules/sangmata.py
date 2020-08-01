# Port to userbot by @KeselekPermen69

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from asyncio.exceptions import TimeoutError
from userbot.events import register
import requests
from userbot import bot, CMD_HELP

@register(outgoing=True, pattern=r"^\.sg(?: |$)(.*)")
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("`Reply to any user message.`")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("`Reply to actual users message.`")
        return
    await steal.edit("`Sit tight while I steal some data from NASA`")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply("`Please unblock @sangmatainfo_bot and try again`")
                return
            if response.text.startswith("No records found"):
                await steal.edit("`No records found for this user`")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"{response.message}")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Error: `@SangMataInfo_bot` is not responding!.`")



CMD_HELP.update(
    {
        "sangmata": ".sg \
          \nUsage: View user history.\n"
    }
)
