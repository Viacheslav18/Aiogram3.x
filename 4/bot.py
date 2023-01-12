import asyncio
import logging
from aiogram import Bot, Dispatcher
from handlers import questions, different_types

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token='your bot token here', parse_mode='HTML')
    dp = Dispatcher()

    dp.include_router(questions.router)
    dp.include_router(different_types.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
