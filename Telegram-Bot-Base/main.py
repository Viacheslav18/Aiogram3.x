import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import router_start, router_inline

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token='@BotFather token', parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(router_start.router)
    dp.include_router(router_inline.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
