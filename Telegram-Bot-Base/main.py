import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import router_start, router_inline

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token='5972749418:AAHruAQ_dn42rzHR_2n4iMtY6MOAubzPK1g', parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(router_start.router)
    dp.include_router(router_inline.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())