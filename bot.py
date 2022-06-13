# Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [BotStatus Telegram bot by TeLe TiPs] (https://github.com/teletips/Powerful_BotStatus-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/Powerful_BotStatus-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name="botstatus_teletips",
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


async def main_teletips():
    async with app:
        while True:
            print("Checking...")
            xxx_teletips = f"📈 **[Breakdowns](https://github.com/breakdowns) Bot Status**\n\n"
            for bot in BOT_LIST:
                name = await app.get_chat(bot)
                try:
                    yyy_teletips = await app.send_message(bot, "/start")
                    aaa = yyy_teletips.id
                    await asyncio.sleep(10)
                    zzz_teletips = app.get_chat_history(bot, limit=1)
                    async for ccc in zzz_teletips:
                        bbb = ccc.id
                    if aaa == bbb:
                        xxx_teletips += f"• 🚫 [{name.first_name}](https://t.me/{bot})\n"
                        for bot_admin_id in BOT_ADMIN_IDS:
                            try:
                                await app.send_message(
                                    int(bot_admin_id),
                                    f"🚨 **@{bot} is down.**",
                                )
                            except Exception:
                                pass
                        await app.read_chat_history(bot)
                    else:
                        xxx_teletips += f"• ✅ [{name.first_name}](https://t.me/{bot})\n"
                        await app.read_chat_history(bot)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
            time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
            last_update = time.strftime(f"{TIME_FORMAT}")
            xxx_teletips += f"\n📶 **Last checked:** __{last_update} ({TIME_ZONE})__\n\nℹ️ **Bot Status Are Auto-Updated Every 3 Hours.**"
            return await app.edit_message_text(
                int(CHANNEL_OR_GROUP_ID),
                MESSAGE_ID,
                xxx_teletips,
                disable_web_page_preview=True,
            )
            # print(f"Last checked on: {last_update}")
            # await asyncio.sleep(6300)


app.run(main_teletips())

# Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
