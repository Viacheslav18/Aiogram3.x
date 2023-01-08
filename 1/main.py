import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.utils.markdown import hlink
from keyboards import *

API_TOKEN = 'your bot token here'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.reply(f"<b>Привіт {message.from_user.full_name}!</b> У нашому боті ти можеш отримувати інформацію, таку як ідентифікатор(ID), ім'я, юзернейм, мову інтерфейсу та інші дані.", reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Text(text='🌐Головне меню'))
async def with_puree(message: types.Message):
    await message.answer('📂Виберіть клавішу, яка вам потрібна', reply_markup=keyboard_main.as_markup(resize_keyboard=True))

@dp.message(Text(text='🎁Получити бонус'))
async def with_puree(message: types.Message):

    GitHub_link = hlink('📁GitHub', 'https://github.com/Viacheslav18/Aiogram3.x/blob/main/1/main.py')
    Lessons_link = hlink('📚Навчальний матеріал, що допомагає створити свого бота', 'https://mastergroosha.github.io/aiogram-3-guide/')
    await message.answer(f"""
🎁У якості бонусу ви можете переглянути код цього бота в відкритому доступі на GitHub або створити свій власний бот з нуля, використовуючи навчальний матеріал.\n
<b>{GitHub_link}</b>
<b>{Lessons_link}</b>""", reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Text(text='🌐Отримати інформацію'))
async def with_puree(message: types.Message):
    await message.answer('📂Виберіть інформацію, яку вам потрібно отримати!', reply_markup=keyboard_info.as_markup(resize_keyboard=True))

@dp.message(Text(text='📮Получити всю інформацію'))
async def all_info(message: types.Message):
    info = (f"➕<b>ID:</b> <code>{message.from_user.id}</code>\n"
            f"➕<b>Ім'я, прізвище:</b> <code>{message.from_user.full_name}</code>\n"
            f"➕<b>Юзернейм:</b> <code>{message.from_user.username}</code>\n"
            f"➕<b>Мова інтерфейсу:</b> <code>{message.from_user.language_code}</code>\n"
            f"➕<b>Чи є у вас Telegram Premium?🌟:</b> <code>{message.from_user.is_premium}</code>\n")
    await message.answer(info)
    await message.delete()

@dp.message(Text(text='🆔ID користувача'))
async def id_info(message: types.Message):
    info = (f"➕<b>ID:</b> <code>{message.from_user.id}</code>\n")
    await message.answer(info)
    await message.delete()

@dp.message(Text(text="👤Ім'я та прізвище"))
async def full_name_info(message: types.Message):
    info = f"➕<b>Ім'я, прізвище:</b> <code>{message.from_user.full_name}</code>\n"
    await message.answer(info)
    await message.delete()

@dp.message(Text(text="🌐Юзернейм"))
async def username_info(message: types.Message):
    info = f"➕<b>Юзернейм:</b> <code>{message.from_user.username}</code>\n"
    await message.answer(info)
    await message.delete()

@dp.message(Text(text="🏳️Мова інтерфейсу"))
async def language_code_info(message: types.Message):
    info = f"➕<b>Мова інтерфейсу:</b> <code>{message.from_user.language_code}</code>\n"
    await message.answer(info)
    await message.delete()

@dp.message(Text(text="↩️Повернутися до головного меню"))
async def language_code_info(message: types.Message):
    await message.answer('Ви повернулись до головного меню↩️', reply_markup=keyboard_main.as_markup(resize_keyboard=True))

@dp.message(Text(text='❓Технічна підтримка'))
async def cmd_faq(message: types.Message):
    await message.answer('Перед тим як звертатися з запитаннями до адміністратора, перевірте, чи не міститься відповідь на них у розділі "❓Питання/Відповідь". Якщо все ж таки там немає відповіді, ви можете написати адміністратору.', reply_markup=keyboard_help_admin.as_markup(resize_keyboard=True))

@dp.message(Text(text='↩️Назад'))
async def cmd_faq(message: types.Message):
    await message.answer('Ви повернулись назад↩️', reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Text(text="📥Зв'язатися з адміністратором через Telegram"))
async def language_code_info(message: types.Message):
    await message.answer("Для зв'язку з адміністратором бота скористайтеся телеграм-контактом @vjacheslav18. Будь ласка, робіть свої питання/пропозиції в одному повідомленні, щоб уникнути створення спаму повідомленнями. Відповідь від адміністратора прийде протягом 24 годин.", reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Text(text="❓Питання/Відповідь"))
async def admin_help(message: types.Message):

    GitHub_link = hlink('GitHub', 'https://github.com/Viacheslav18/Aiogram3.x/blob/main/1/main.py')

    answers = (f"""
<b>Питання:</b> Що вміє ваш бот і для чого він взагалі?
<b>Відповідь:</b> У нашому боті ти можеш отримувати інформацію, таку як ідентифікатор(ID), ім'я, юзернейм, мову інтерфейсу та інші дані.

<b>Питання:</b> Де можна переглянути код цього бота в відкритому доступі?
<b>Відповідь:</b> Ви можете переглянути код цього бота в відкритому доступі на {GitHub_link} 
        """) 

    await message.answer(f"<b>📂Відповіді на самі популярні питання</b> \n{answers}", reply_markup=keyboard_help_admin.as_markup(resize_keyboard=True))
    await message.delete()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
