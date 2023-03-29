from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, Text
from keyboards.start_reply import *
from keyboards.start_inline import *

router = Router()

@router.message(Command(commands=['start']))
async def command_start(message: Message):
    await message.answer('Hello!', reply_markup=reply_keyboard.as_markup(resize_keyboard=True))

@router.message(Text(text='Start keyboard'))
async def start_keyboard(message: Message):
    await message.answer('Start keyboard!)', reply_markup=inline_keyboard.as_markup(resize_keyboard=True))