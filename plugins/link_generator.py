#(©)Codexbotz

from pyrogram import Client, filters
from pyrogram.types import Message
from bot import Bot
from config import ADMINS
from helper_func import encode, get_message_id
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
            pehla_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send 480P Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
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
            dusra_message = await client.ask(text = "Forward Message from the DB Channel (with Quotes)..\nor Send 720P Post link", chat_id = message.from_user.id, filters=(filters.forwarded | (filters.text & ~filters.forwarded)), timeout=60)
        except:
            return
        second_msg_id = await get_message_id(client, dusra_message)
        if second_msg_id:
            break
        else:
            await dusra_message.reply("❌ Error\n\nthis Forwarded Post is not from my DB Channel or this Link is not taken from DB Channel", quote = True)
            continue

    first_base64_string = await encode(f"get-{first_msg_id * abs(client.db_channel.id)}")
    first_link = await get_shortlink(f"https://telegram.me/{client.username}?start={first_base64_string}")
    second_base64_string = await encode(f"get-{second_msg_id * abs(client.db_channel.id)}")
    second_link = await get_shortlink(f"https://telegram.me/{client.username}?start={second_base64_string}")
    await dusra_message.reply_text(f"🎬 𝐓𝐢𝐭𝐥𝐞:
🔊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: <b>English + Hindi</b>
🎞 𝐐𝐮𝐚𝐥𝐢𝐭𝐲: <b>Web-Rip</b>
📧 𝐒𝐮𝐛𝐭𝐢𝐭𝐥𝐞𝐬: <b>Esubs</b>
<b>〰〰〰〰〰〰〰〰〰〰〰
🧑‍💻How to Download :
Watch </b>👉 <b>https://t.me/HeavenForYouAll/8261</b>
<b>〰〰〰〰〰〰〰〰〰〰〰

480p x264 [ MB ]
👉 {first_link}

720p x265 [ MB ]
👉 {second_link}

720p x264 [ GB ]
👉 

1080p x264 [ GB ]
👉 

.........................................................
🎯 Join : </b>@HeavenForYouAll
<b>🎯 Join : </b>@HeavenRequest
<b>---------------------------------------------
To get Latest Movies/Series faster with Ad-free experience, get your Premium membership through </b>@HeavenPremiumBot<b>.
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°</b>
", quote=True)
