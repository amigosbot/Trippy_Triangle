import asyncio
from time import time
from datetime import datetime
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9dba7ece56cb7d22f383d.jpg",
        caption=f"""**Let's enjoy the Vibe with un-stopable 🎶 without any Lag and struck.\n\n It's a official Music bot of [༄A͎m͎i͎g͎o͎s͎࿐](https://t.me/amigozzworld) \n\nNB: Bot and Userbot are locked by owner ,
🧾COMMANDS🧾 \n\nCommon Commands - `\play` \n\nAdmin Commands - `/pause`,`/skip`,`/resume`,`/end, /stop`,`restart`

Join and Support our Group and Channel
**""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔱🅖🅡🅞🅤🅟🔱", url=f"https://t.me/amigozzworld"),
                    InlineKeyboardButton(
                        "🌠ᴄʜᴀɴɴᴇʟ🌠", url=f"https://t.me/trippyworld_420"),
                    InlineKeyboardButton(
                        "🎶Oᴡɴᴇʀ🎶", url=f"https://t.me/Trippy_Trippy"),
                ]
            ]
        ),
     )
    
    
@Client.on_message(commandpro(["/start", "/alive", "blackcat"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/9dba7ece56cb7d22f383d.jpg",
        caption=f"""**Me on Ultra Fast,Laggless, and No struck** \n🥀Commands🥀 \n\n`/play` \n\n\`/pause` \n\n`/resume` \n\n`/skip` \n\n`/restart` \n\nadmins only - `pause,resume,restart,skip`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏍️TrippY🏍️", url=f"https://t.me/Trippy_Trippy"),
                    InlineKeyboardButton(
                        "🎶ChanneL🎶", url=f"https://t.me/trippyworld_420"),
                ]
            ]
        ),
    )

