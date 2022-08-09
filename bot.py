from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name="botstatus_breakdowns",
    api_id=int(os.environ["API_ID"]),
    api_hash=os.environ["API_HASH"],
    session_string=os.environ["SESSION_STRING"],
)
TIME_ZONE = os.environ["TIME_ZONE"]
TIME_FORMAT = os.environ["TIME_FORMAT"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(" ")]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(" ")]


async def main_breakdowns():
    async with app:
        while True:
            print("Checking...")
            xxx_breakdowns = f"📈 **[Breakdowns](https://github.com/breakdowns) Bot Status**\n\n"
            for bot in BOT_LIST:
                name = await app.get_chat(bot)
                try:
                    yyy_breakdowns = await app.send_message(bot, "/start")
                    aaa = yyy_breakdowns.id
                    await asyncio.sleep(10)
                    zzz_breakdowns = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_breakdowns:
                        bbb = ccc.id
                    if aaa == bbb:
                        xxx_breakdowns += f"• 🚫 [{name.first_name}](https://t.me/{bot})\n"
                    else:
                        xxx_breakdowns += f"• ✅ [{name.first_name}](https://t.me/{bot})\n"
                    await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"{TIME_FORMAT}")
            xxx_breakdowns += f"\n📶 **Last checked:** __{last_update} ({TIME_ZONE})__\n\nℹ️ **Bot Status Are Auto-Updated Every 3 Hours.**"
            return await app.edit_message_text(
                int(CHANNEL_OR_GROUP_ID),
                MESSAGE_ID,
                xxx_breakdowns,
                disable_web_page_preview=True,
            )


app.run(main_breakdowns())
