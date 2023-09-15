import asyncio
import random
from pyrogram import *
from pyrogram.errors import *
from pyrogram.raw.functions.messages import *
from pyrogram.types import *
from pyrogram.dispatcher import *

from Magic import *

#from Magic.utils import eor, extract_user


@ubot.on_message(filters.command(["sa"], ".") & filters.me)
async def sang(client: Client, message: Message):
   # kimak = await extract_user(message)
    lonte = await message.reply("Sedang Memproses...")
    if client:
        try:
            user = await client.get_users(client)
        except Exception as error:
        return await client.loop(error)
    bot = ["@Sangmata_bot", "@SangMata_beta_bot"]
    getbot = random.choice(bot)
    try:
        txt = await client.send_message(getbot, f"{user.id}")
    except YouBlockedUser:
        await client.unblock_user(getbot)
        txt = await client.send_message(getbot, f"{user.id}")
    await txt.delete()
    await asyncio.sleep(5)
    await client.delete()
    async for stalk in client.search_messages(getbot, query="History", limit=2):
        if not stalk:
            NotFound = await client.send_message(client.me.id, "Tidak ada komentar")
            await NotFound.delete()
        elif stalk:
            await message.reply(stalk.text)
    user_info = await client.resolve_peer(getbot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
