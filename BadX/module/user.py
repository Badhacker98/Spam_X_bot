import os

from . import TheBadX

from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command(["setpic", "updatepic"], prefixes=TheBadX.handler))
async def set_profile(BadX: Client, message: Message):
    if BadX.me.is_bot:
        return
    if await TheBadX.sudo.sudoFilter(message, 1):
        return
    replied = message.reply_to_message
    media_path = "BadX/resources/Profile.jpg"
    if (replied and replied.media and (replied.photo or (replied.document and "image" in replied.document.mime_type))):
            await BadX.download_media(message=replied, file_name=media_path)
            await BadX.set_profile_photo(photo=media_path)
            await message.reply(f"**Changed profile picture successfully** ✅")
            if os.path.exists(media_path):
                os.remove(media_path)
    else:
        await message.reply("__Reply To any Photo To Change Profile pic__")

@Client.on_message(filters.command(["setname", "updatename"], prefixes=TheBadX.handler))
async def set_name(BadX: Client, message: Message):
    if BadX.me.is_bot:
        return
    if await TheBadX.sudo.sudoFilter(message, 1):
        return
    args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
    if message.reply_to_message:
        name = str(message.reply_to_message.text)
    elif len(args) != 0:
        name = str(args[0])
    else:
        await message.reply(f"**Wrong usage!** \n __- syntax:__ `{TheBadX.handler}setname` (name)")
        return
    try:
        await BadX.update_profile(first_name=name)
        await message.reply(f"**✅ Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
    except Exception as ex:
        await message.reply(f"**Error !!** \n\n {ex}")

@Client.on_message(filters.command(["setall", "updateall"], prefixes=TheBadX.handler))
async def set_all(BadX: Client, message: Message):
    if BadX.me.is_bot:
        return
    if await TheBadX.sudo.sudoFilter(message, 1):
        return
    args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
    if message.reply_to_message:
        x_name = str(message.reply_to_message.text)
    elif len(args) != 0:
        x_name = str(args[0])
    else:
        await message.reply(f"**Wrong usage!** \n __- syntax:__ `{TheBadX.handler}setall` (name)")
        return
    wait = await message.reply("__updating....__")
    client_position = 1
    for c in TheBadX.clients:
        if c.me.id == BadX.me.id:
            break
        else:
            client_position += 1

    if client_position:
        name = f"#{client_position} - {x_name}"
    else:
        name = x_name
    try:
        await BadX.update_profile(first_name=name)
        await message.reply(f"**✅ Profile Name Changed Successfully !!** \n\n **New Name:** {name}")
    except Exception as ex:
        await message.reply(f"**Error !!** \n\n {ex}")
    await wait.delete()


@Client.on_message(filters.command(["setbio", "updatebio"], prefixes=TheBadX.handler))
async def set_bio(BadX: Client, message: Message):
    if BadX.me.is_bot:
        return
    if await TheBadX.sudo.sudoFilter(message, 1):
        return
    args = "".join(message.text.split(maxsplit=1)[1:]).split(" ", 0)
    if message.reply_to_message:
        bio = str(message.reply_to_message.text)
    elif len(args) != 0:
        bio = str(args[0])
    else:
        await message.reply(f"**Wrong usage!** \n __- syntax:__ `{TheBadX.handler}setbio` (bio)")
        return
    try:
        await BadX.update_profile(bio=bio)
        await message.reply(f"**✅ Profile Name Changed Successfully !!** \n\n **New bio:** {bio}")
    except Exception as ex:
        await message.reply(f"**Error !!** \n\n {ex}")