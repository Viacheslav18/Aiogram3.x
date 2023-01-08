import asyncio
import logging
import time
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.utils.markdown import hlink
from kb import *

API_TOKEN = "your bot token here"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):

    IT_link = hlink('😎Посилання на дуже лютого айтішника', 'https://t.me/vjacheslav18')
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHLbJjuytm_DVv3XFB38GiUI6V9lWMOAACzw8AAuZ3mEuzyIsRyz1m6y0E')
    await message.reply(f"<b>Привіт {message.from_user.full_name}!</b> Це дуже крутий бот, який розробив лютий айтішник\n\n <b>{IT_link}</b>", reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Command(commands='update'))
async def cmd_update(message: types.Message):
    await message.answer('📂Вас переадресовувало в головне меню', reply_markup=keyboard_main.as_markup(resize_keyboard=True))

@dp.message(Text(text='Запустити бота🤖'))
async def bot_start(message: types.Message):
    await message.answer('<b>Щоб користуватись ботом потрібно пройти перевірку❗️</b>\n\nВи є чи були колись токсіком?', reply_markup=keyboard_toksik_checker.as_markup(resize_keyboard=True))

@dp.message(Text(text='Так, я токсік😈'))
async def check_toksik_1(message: types.Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHLbZjuywiGUlSbfJrO9qTnB4nx0pgAwACCRgAAmJyKUgT4jYn53Cj2C0E')
    await message.answer('<b>Вибачте, але токсікам заборонено користуватись ботом⛔️</b>', reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Text(text='Ні, я дуже добра душа😇'))
async def check_toksik_2(message: types.Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHLbhjuyyWWuadaFS9pFnc7yrS-sosqQACMwAD_wzODBWQZxnEDXByLQQ')
    await message.answer(f'🌐<b>Вітаю в головному меню {message.from_user.full_name}</b>\n\n<i>Приємно мати справу з розумними дітьми😘</i>', reply_markup=keyboard_main.as_markup(resize_keyboard=True))

@dp.message(Text(text='🧠Проходити опитування'))
async def quiz(message: types.Message):
    await message.answer("🧠Оберіть рівень складності опитування", reply_markup=keyboard_quiz_difficult.as_markup(resize_keyboard=True))

@dp.message(Text(text='Легкий😇'))
async def easy_level(message: types.Message):
    await message.answer("🧠Виберіть рівень", reply_markup=keyboard_easy.as_markup(resize_keyboard=True))

@dp.message(Text(text='1😇'))
async def easy_level_1(message: types.Message):
    await message.answer('<b>На даний момент ця кнопка не має функціоналу⛔️\n\nЩоб виходили обновлення нашого бота, необхідно підтримувати цей проект. Ми надіємось на фідбек і нові пропозиції для бота.</b>', reply_markup=keyboard_easy.as_markup(resize_keyboard=True))

@dp.message(Text(text='2😇'))
async def easy_level_2(message: types.Message):
    await message.answer('<b>На даний момент ця кнопка не має функціоналу⛔️\n\nЩоб виходили обновлення нашого бота, необхідно підтримувати цей проект. Ми надіємось на фідбек і нові пропозиції для бота.</b>', reply_markup=keyboard_easy.as_markup(resize_keyboard=True))

@dp.message(Text(text='3😇'))
async def easy_level_3(message: types.Message):
    await message.answer('<b>На даний момент ця кнопка не має функціоналу⛔️\n\nЩоб виходили обновлення нашого бота, необхідно підтримувати цей проект. Ми надіємось на фідбек і нові пропозиції для бота.</b>', reply_markup=keyboard_easy.as_markup(resize_keyboard=True))

@dp.message(Text(text='4😇'))
async def easy_level_4(message: types.Message):
    await message.answer('<b>На даний момент ця кнопка не має функціоналу⛔️\n\nЩоб виходили обновлення нашого бота, необхідно підтримувати цей проект. Ми надіємось на фідбек і нові пропозиції для бота.</b>', reply_markup=keyboard_easy.as_markup(resize_keyboard=True))

@dp.message(Text(text='Середній😜'))
async def medium_level(message: types.Message):
    await message.answer("<b>На даний момент у вас недостатньо інтелектуальних ресурсів, щоб проходити ці опитування⛔️</b>")
    await message.delete()

@dp.message(Text(text='Важкий🥶'))
async def hard_level(message: types.Message):
    await message.answer("<b>На даний момент у вас недостатньо інтелектуальних ресурсів, щоб проходити ці опитування⛔️</b>")
    await message.delete()

@dp.message(Text(text='Надзвичайно важкий😈'))
async def very_hard_level(message: types.Message):
    await message.answer("<b>На даний момент у вас недостатньо інтелектуальних ресурсів, щоб проходити ці опитування⛔️</b>\n\n<i>❗️Доступно лише тим хто навчається в розумному класі</i>")
    await message.delete()

@dp.message(Text(text='🧠Змінити рівень складності'))
async def change_quiz(message: types.Message):
    await message.answer("🧠Оберіть рівень складності опитування", reply_markup=keyboard_quiz_difficult.as_markup(resize_keyboard=True))
    await message.delete()

@dp.message(Text(text='Повернутися до головного меню↩️'))
async def back_main_menu(message: types.Message):
    await message.answer(f"📂{message.from_user.first_name}, ви були переадресовані в головне меню", reply_markup=keyboard_main.as_markup(resize_keyboard=True))

@dp.message(Text(text='Колись можливо буде🔜'))
async def check_toksik_1(message: types.Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHLh9juzvhnNTZCD5MLfVqR1cojHIglgACgxkAAvAtWEjyPMatZ5a8Zy0E')
    await message.answer('<b>На даний момент ця кнопка не має функціоналу⛔️\n\nЩоб виходили обновлення нашого бота, необхідно підтримувати цей проект. Ми надіємось на фідбек і нові пропозиції для бота.</b>', reply_markup=keyboard_main.as_markup(resize_keyboard=True))

@dp.message(Text(text='💰Реклама №1'))
async def reklama_1(message: types.Message):
    await message.answer(f"""
🚨<b>{message.from_user.first_name}</b> тут могла бути ваша реклама

<b>✅Спонсор показу цієї реклами: <i>Адміністрація бота</i></b>""")
    await message.answer('<b>Реклама закінчиться через 10 секунд.....</b>🎥')
    time.sleep(5)
    await message.answer('<b>Реклама закінчиться через 5 секунд.....</b>🎥')
    time.sleep(5)
    await message.answer(f'<b>Реклама №1 закінчилась!✅\n\n{message.from_user.first_name}</b> ви подивились рекламу та получаєте за це + до карми🎁')

@dp.message(Text(text='💰Реклама №2'))
async def reklama_2(message: types.Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHLcpjuy1iCXSUYDMIRGcpCbi6ROOJ3QACZRsAAp6nSUrnP7r6oe6tzC0E')
    await message.answer(f"""
🚨<b>{message.from_user.first_name}</b> тут могла бути ваша реклама

<b>✅Спонсор показу цієї реклами: <i>Адміністрація бота</i></b>""")
    await message.answer('<b>Реклама закінчиться через 10 секунд.....</b>🎥')
    time.sleep(5)
    await message.answer('<b>Реклама закінчиться через 5 секунд.....</b>🎥')
    time.sleep(15)
    await message.answer_sticker(sticker='CAACAgIAAxkBAAEHLchjuy1Ysdux6HX1CxyDNbHQpd61-QACEiIAAhkLWUt0jQWPnUbWuS0E')
    await message.answer(f'<b>Реклама №2 закінчилась!✅\n\n{message.from_user.first_name}</b> ви подивились рекламу та получаєте за це + до карми🎁')

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())