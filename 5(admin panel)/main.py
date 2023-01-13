import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import router_all, router_start, router_other

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token='token', parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(router_start.router)
    dp.include_router(router_all.router)
    dp.include_router(router_other.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
