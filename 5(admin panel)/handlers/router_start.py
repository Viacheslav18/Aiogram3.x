from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.keyboard_user import keyboard_user_start
from keyboards.keyboard_admin import keyboard_admin_start

router = Router()

@router.message(Command(commands=['start']))
async def cmd_start(message: Message):

    if message.from_user.id == 827612750:
        await message.answer(f'Привіт {message.from_user.first_name}!', reply_markup=keyboard_admin_start())
    else:
        await message.answer(f'Привіт {message.from_user.first_name}!', reply_markup=keyboard_user_start())

@router.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.reply('<b>⚠️Щоб перезагрузити бота використовуйте команду <i>/start</i></b>')