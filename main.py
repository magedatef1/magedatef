import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from database import init_db

from bot.start import router as start_router
from bot.menu import router as menu_router
from bot.publish import router as publish_router
from bot.posts import router as posts_router
from bot.analytics import router as analytics_router
from bot.accounts import router as accounts_router
from bot.scheduler import router as scheduler_router
from bot.comments import router as comments_router
from bot.media import router as media_router
from bot.settings import router as settings_router


async def main():
    init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(publish_router)
    dp.include_router(posts_router)
    dp.include_router(analytics_router)
    dp.include_router(accounts_router)
    dp.include_router(scheduler_router)
    dp.include_router(comments_router)
    dp.include_router(media_router)
    dp.include_router(settings_router)

    print("Maged Atef Bot started...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
