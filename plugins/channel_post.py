import asyncio
from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
from utils import get_shortlink

from bot import Bot
from config import ADMINS, CHANNEL_ID, DISABLE_CHANNEL_BUTTON
from helper_func import encode

@Bot.on_message(filters.private & filters.user(ADMINS) & ~filters.command(['start','users','broadcast','batch','genlink','stats']))
async def channel_post(client: Client, messageone: Message):
    reply_text = await message.reply_text("send 480p file", quote = True)
async def channel_post(client: Client, messagetwo: Message):
    reply_text = await message.reply_text("send 720p file", quote = True)
    try:
        post_message = await messageone.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_message = await messagetwo.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong for 480p file")
        return
    post_messageone = await messagetwo.copy(chat_id = client.db_channel.id, disable_notification=True)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        post_messagetwo = await messagetwo.copy(chat_id = client.db_channel.id, disable_notification=True)
    except Exception as e:
        print(e)
        await reply_text.edit_text("Something went Wrong for 720p file!")
        return
    converted_idone = post_messageone.id * abs(client.db_channel.id)
    stringone = f"get-{converted_idone}"
    base64_stringone = await encode(stringone)
    linkone = await get_shortlink(f"https://telegram.me/{client.username}?start={base64_stringone}")
    converted_idtwo = post_messagetwo.id * abs(client.db_channel.id)
    stringtwo = f"get-{converted_idtwo}"
    base64_stringtwo = await encode(stringtwo)
    linktwo = await get_shortlink(f"https://telegram.me/{client.username}?start={base64_stringtwo}")

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://t.me/share/Targetx25')]])

    await reply_text.edit(f"🎬 𝐓𝐢𝐭𝐥𝐞:
🔊 𝐋𝐚𝐧𝐠𝐮𝐚𝐠𝐞: English + Hindi
🎞 𝐐𝐮𝐚𝐥𝐢𝐭𝐲: Web-Rip
📧 𝐒𝐮𝐛𝐭𝐢𝐭𝐥𝐞𝐬: Esubs
〰〰〰〰〰〰〰〰〰〰〰
🧑‍💻How to Download :
Watch 👉 https://t.me/HeavenForYouAll/8261
〰〰〰〰〰〰〰〰〰〰〰

480p x264 [ MB ]
👉 {linkone}

720p x265 [ MB ]
👉 

720p x264 [ GB ]
👉 {linktwo}

1080p x264 [ GB ]
👉 

.........................................................
🎯 Join : @HeavenForYouAll
🎯 Join : @HeavenRequest
---------------------------------------------
To get Latest Movies/Series faster with Ad-free experience, get your Premium membership through @HeavenPremiumBot.
°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°° ", 
reply_markup=reply_markup, disable_web_page_preview = True)

    if not DISABLE_CHANNEL_BUTTON:
        await post_message.edit_reply_markup(reply_markup)

@Bot.on_message(filters.channel & filters.incoming & filters.chat(CHANNEL_ID))
async def new_post(client: Client, message: Message):

    if DISABLE_CHANNEL_BUTTON:
        return

    converted_idone = post_messageone.id * abs(client.db_channel.id)
    stringone = f"get-{converted_idone}"
    base64_stringone = await encode(stringone)
    linkone = await get_shortlink(f"https://telegram.me/{client.username}?start={base64_stringone}")
    converted_idtwo = post_messagetwo.id * abs(client.db_channel.id)
    stringtwo = f"get-{converted_idtwo}"
    base64_stringtwo = await encode(stringtwo)
    linktwo = await get_shortlink(f"https://telegram.me/{client.username}?start={base64_stringtwo}")

    reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Share URL", url=f'https://t.me/share/Targetx25')]])
    try:
        await messagetwo.edit_reply_markup(reply_markup)
    except Exception as e:
        print(e)
        pass
