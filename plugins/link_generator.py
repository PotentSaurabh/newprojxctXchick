#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id, get_message_mg
from utils import get_shortlink

@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('batch'))
async def batch(client: Client, message: Message):
    while True:
        try:
            first_message = await client.ask(text = "Forward the First Message from DB Channel (with Quotes)..\n\nor Send the DB Channel Post Link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        f_msg_id = await get_message_id(client, first_message)
        if f_msg_id:
            break
        else:
            await first_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue

    while True:
        try:
            second_message = await client.ask(text = "Forward the Last Message from DB Channel (with Quotes)..\nor Send the DB Channel Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        s_msg_id = await get_message_id(client, second_message)
        if s_msg_id:
            break
        else:
            await second_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is taken from DB Channel", quote = True)
            continue


    string = f"get-{f_msg_id * abs(client.db_channel.id)}-{s_msg_id * abs(client.db_channel.id)}"
    base64_string = await encode(string)
    link =  await get_shortlink(f"https://telegram.me/{client.username}?start={base64_string}")
    await second_message.reply_text(f"<b>Here is your link</b>\n\n{link}", quote=True)


@Bot.on_message(filters.private & filters.user(ADMINS) & filters.command('genlink'))
async def link_generator(client: Client, message: Message):
    while True:
        try:
            pehla_message = await client.ask(text = "Send 480P Post File", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        first_msg_id = await get_message_id(client, pehla_message)
        if first_msg_id:
            break
        else:
            await pehla_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
            
            
    while True:
        try:
            dusra_message = await client.ask(text = "Send 720P HEVC File", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        second_msg_id = await get_message_id(client, dusra_message)
        if second_msg_id:
            break
        else:
            await dusra_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
     
    while True:
        try:
            tesra_message = await client.ask(text = "Send 720P X264 File", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        third_msg_id = await get_message_id(client, tesra_message)
        if third_msg_id:
            break
        else:
            await tesra_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue
    
    while True:
        try:
            chautha_message = await client.ask(text = "Send 1080P X264 File", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        fourth_msg_id = await get_message_id(client, chautha_message)
        if fourth_msg_id:
            break
        else:
            await chautha_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True) 
            continue
            
    while True:
        try:
            panchma_message = await client.ask(text = "Send Movie name", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        fifth_msg_id = await get_message_mg(client, panchma_message)
        if fifth_msg_id:
            break
        else:
            await panchma_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    first_base64_string = await encode(f"get-{first_msg_id * abs(client.db_channel.id)}")
    first_link = await get_shortlink(f"https://telegram.me/{client.username}?start={first_base64_string}")
    second_base64_string = await encode(f"get-{second_msg_id * abs(client.db_channel.id)}")
    second_link = await get_shortlink(f"https://telegram.me/{client.username}?start={second_base64_string}")
    third_base64_string = await encode(f"get-{third_msg_id * abs(client.db_channel.id)}")
    third_link = await get_shortlink(f"https://telegram.me/{client.username}?start={third_base64_string}")
    fourth_base64_string = await encode(f"get-{fourth_msg_id * abs(client.db_channel.id)}")
    fourth_link = await get_shortlink(f"https://telegram.me/{client.username}?start={fourth_base64_string}")
    await panchma_message.reply_text(f"🎬 𝐓𝐢𝐭𝐥𝐞:{fifth_msg_id}\n🔊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞:\n🎞 𝐐𝐮𝐚𝐥𝐢𝐭𝐲:\n<b>〰〰〰〰〰〰〰〰〰〰〰\n🧑‍💻How to Download :\nWatch </b>👉\n<b>https://t.me/HeavenForYouAll/7878</b>\n<b>〰〰〰〰〰〰〰〰〰〰〰\n\n480p x264 []\n👉{first_link}\n\n720p x265 []\n👉{second_link}\n\n720p x264 []\n👉{third_link}\n\n1080p x264 []\n👉{fourth_link}\n\n.........................................................\n🎯 Join :\n</b><b>@HeavenForYouAll</b>\n<b>🎯 Join : </b><b>@HeavenRequest</b>\n<b>---------------------------------------------\nTo get Latest Movies/Series faster with Ad-free experience, get your Premium membership through </b><b>@HeavenPremiumBot</b><b>.\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°</b>", quote=True)
