from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Text
from keyboards.keyboard_admin import keyboard_admin_start, keyboard_admin_adminka, keyboard_admin_back

router = Router()

@router.message(Text(text='✅Почати користуватися ботом'))
async def bot_start(message: Message):
    await message.answer(f'<b>Привіт <i>{message.from_user.first_name}</i>! Якщо є любі питання пиши: <i>@vyacheesIav</i></b>')

@router.message(Text(text='Панель адміністратора🛠'))
async def admin_panel(message: Message):

    if message.from_user.id == 827612750:
        await message.answer(f'<b>{message.from_user.first_name} вітаю в панелі адміністратора🛠</b>', reply_markup=keyboard_admin_back())
        await message.answer(f'<i>Щоб вийти з панелі адміністратора виберіть кнопку "Назад↩️"</i>' ,reply_markup=keyboard_admin_adminka())
    else:
        await message.answer(f'<b>{message.from_user.first_name} ви не є адміном, тому не можете користуватись цим!</b>')

@router.message(Text(text='Назад↩️'))
async def admin_panel(message: Message):
    await message.answer(f'<b>Ви повернулись до головного меню↩️</b>', reply_markup=keyboard_admin_start())