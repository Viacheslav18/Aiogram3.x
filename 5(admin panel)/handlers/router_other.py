from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def other_message(message: Message):
    await message.answer('<b>🚫Я не знаю, як на це відповісти! Використайте команду <i>/help</i></b>')