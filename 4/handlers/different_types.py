from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer('Ви відправили текстове повідомлення!')

@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer('Ви відправили стікер!')

@router.message(F.audio)
async def message_with_gif(message: Message):
    await message.answer('Ви відправили аудіо файл!')

@router.message(F.video)
async def message_with_gif(message: Message):
    await message.answer('Ви відправили відео!')

@router.message()
async def message_not_command(message: Message):
    await message.answer('🚫Я не знаю як вам відповісти на це! Скористайтесь командою /help')