import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN غير موجود. ضع التوكن داخل ملف .env"
    )

if OWNER_ID == 0:
    raise RuntimeError(
        "OWNER_ID غير موجود. ضع Telegram ID داخل .env"
    )
