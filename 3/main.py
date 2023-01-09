import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, Text
from aiogram.utils.markdown import hlink
from keyboard import *
from quiz import *

API_TOKEN = "5942246856:AAGGFOERdDAlaXq9P4FRk6F24N7dqk3a5Q8"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN, parse_mode='HTML')
dp = Dispatcher()

@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.reply(f"👋<b>Привіт {message.from_user.full_name}!\n\n🧩Наш бот з вікторинами - це інтелектуальний співрозмовник, який допомагає гравцям розвивати свої знання і навички у різних областях. З його допомогою ви зможете пройти серію цікавих і викликаючих вікторин, які дадуть вам можливість показати свої знання і заробити бали. Бот має багатство цікавих і новинкових вікторин, які зацікавлять та розвиватимуть вас. Не важко з ним почати грати - просто запросіть вікторину і він пропонує варіанти для гри. З ботом вікторин ніколи не буде скучною!</b>😏", reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Text(text='🧩Вікторини'))
async def start_quiz(message: types.Message):
    await message.answer(f"🕹<b>Почнемо вікторину? Виберіть режим вікторини, який вас цікавить</b>", reply_markup=keyboard_quiz.as_markup(resize_keyboard=True))

@dp.message(Text(text='🌍Географічні вікторини'))
async def quiz_flag(message: types.Message):
    await message.answer(f"🌍<b>Географічні вікторини!</b>", reply_markup=keyboard_geography.as_markup(resize_keyboard=True))

@dp.message(Text(text='⚽️Футбольні вікторини'))
async def quiz_flag(message: types.Message):
    await message.answer(f"⚽️<b>Футбольні вікторини!</b>", reply_markup=keyboard_football.as_markup(resize_keyboard=True))

@dp.message(Text(text='🏳️Відгадай прапор'))
async def quiz_flag(message: types.Message):
    await message.answer(f"🏳️<b>Вікторина 'Відгадай прапор'. Ми показуємо вам прапор і даємо декілька варіантів відповідей, а ви обираєте ту, яку схоже найбільше. Спробуйте угадати якомога більше прапорів!</b>", reply_markup=keyboard_quiz_flag.as_markup(resize_keyboard=True))

@dp.message(Text(text='⚽️хз як назвати'))
async def quiz_flag(message: types.Message):
    await message.answer(f"⚽️<b>Футбольні вікторини!</b>", reply_markup=keyboard_quiz_football.as_markup(resize_keyboard=True))

@dp.message(Text(text='🏳️Відправити вікторину'))
async def send_quiz_flag(message: types.Message):
    await message.delete()

    quiz1_txt = 'Якої країни цей прапор?🇺🇦'
    quiz1_choices = ['Україна', 'Франція', 'Туреччина', 'Іспанія']
    quiz1_id = 0
    quiz1 = quiz1_txt, quiz1_choices, quiz1_id

    quiz2_txt = 'Якої країни цей прапор?🇨🇦'
    quiz2_choices = ['США', 'Мексика', 'Канада', 'Сінгапуру']
    quiz2_id = 2
    quiz2 = quiz2_txt, quiz2_choices, quiz2_id

    quiz3_txt = 'Якої країни цей прапор?🇨🇳'
    quiz3_choices = ['Африка', 'Індія', 'Японія', 'Китай']
    quiz3_id = 3
    quiz3 = quiz3_txt, quiz3_choices, quiz3_id

    quiz4_txt = 'Якої країни цей прапор?🇨🇿'
    quiz4_choices = ['Нідерланди', 'Чехія', 'Угорщина', 'Велика Британія']
    quiz4_id = 1
    quiz4 = quiz4_txt, quiz4_choices, quiz4_id

    quiz5_txt = 'Якої країни цей прапор?🇱🇻'
    quiz5_choices = ['Польща', 'Північна Корея', 'Латвія', 'Єгипет']
    quiz5_id = 2
    quiz5 = quiz5_txt, quiz5_choices, quiz5_id

    quiz6_txt = 'Якої країни цей прапор?🏳️‍🌈'
    quiz6_choices = ['ₚосія', 'ЛГБТ', 'Крупкоподібний вид населення']
    quiz6_id = 2
    quiz6 = quiz6_txt, quiz6_choices, quiz6_id

    quiz7_txt = 'Якої країни цей прапор?🇧🇷'
    quiz7_choices = ['Індія', 'Канада', 'Бразилія', 'Іспанія']
    quiz7_id = 2
    quiz7 = quiz7_txt, quiz7_choices, quiz7_id

    quiz8_txt = 'Якої країни цей прапор?🇪🇸'
    quiz8_choices = ['Єгипет', 'Туреччина', 'Китай', 'Іспанія']
    quiz8_id = 3
    quiz8 = quiz8_txt, quiz8_choices, quiz8_id

    quiz9_txt = 'Якої країни цей прапор?🇬🇷'
    quiz9_choices = ['Канада', 'Німеччина ', 'Греція', 'Туреччина']
    quiz9_id = 2
    quiz9 = quiz9_txt, quiz9_choices, quiz9_id

    quiz10_txt = 'Якої країни цей прапор?🇮🇱'
    quiz10_choices = ['Канада', 'Ізраїль', 'Ірландія', 'Ісландія']
    quiz10_id = 1
    quiz10 = quiz10_txt, quiz10_choices, quiz10_id

    all_quiz = [quiz1, quiz2, quiz3, quiz4, quiz5, quiz6, quiz7, quiz8, quiz9, quiz10]
    random_quiz = random.choice(all_quiz)

    question, choices, correct_option_id = random_quiz
    await bot.send_poll(message.chat.id, question=question, options=choices, type='quiz', correct_option_id=correct_option_id)

@dp.message(Text(text='⚽️Відправити вікторину'))
async def send_quiz_flag(message: types.Message):
    await message.delete()

    quiz1_txt = 'Шахтар-Уфа-Манчестер Сіті-Арсенал'
    quiz1_choices = ['Зінченко', 'Марлос', 'Миколенко', 'Мілевський']
    quiz1_id = 0
    quiz1 = quiz1_txt, quiz1_choices, quiz1_id

    quiz2_txt = 'Мальме-Аякс-Ювентус-Інтер-Барселона-Мілан-ПСЖ-Манчестер Юнайтед-Лос Анджелес Гелаксі-Мілан'
    quiz2_choices = ['Ібрагімович', 'Суарез', 'Жиру', 'Болателі']
    quiz2_id = 0
    quiz2 = quiz2_txt, quiz2_choices, quiz2_id

    all_quiz = [quiz1, quiz2]
    random_quiz = random.choice(all_quiz)

    question, choices, correct_option_id = random_quiz
    await bot.send_poll(message.chat.id, question=question, options=choices, type='quiz', correct_option_id=correct_option_id)

@dp.message(Text(text='⚽️Відгадай футболіста по фотографії'))
async def send_quiz_football(message: types.Message):
    await message.answer(f"🚫<b>{message.from_user.first_name}, ця функція в розробці!</b>")

@dp.message(Text(text='⚙️Додаткові функції'))
async def functions(message: types.Message):
    await message.answer(f"⚠️<b>{message.from_user.first_name}, режим '⚙️Додаткові функції' є в розробці, тому може містити баги або не працювати належним чином!</b>", reply_markup=keyboard_functions.as_markup(resize_keyboard=True))

@dp.message(Text(text='🧩Створити вікторину'))
async def functions_create_quiz(message: types.Message):
    await message.answer(f"⚠️<b>{message.from_user.first_name}, режим '⚙️Додаткові функції' є в розробці, тому може містити баги або не працювати належним чином!</b>", reply_markup=keyboard_functions_new_quiz.as_markup(resize_keyboard=True))

@dp.message(Text(text='📥Надіслати вікторину адміну бота'))
async def functions_send_quiz(message: types.Message):
    await message.answer(f"🤝<b>{message.from_user.first_name}, щоб надіслати вікторину адміну бота, напишіть сюди - @vjacheslav18!</b>")

@dp.message(Text(text='🚫Завершити проходження вікторини'))
async def stop_quiz(message: types.Message):
    await message.answer("📂<b>Проходження вікторини було завершено</b>", reply_markup=keyboard_start.as_markup(resize_keyboard=True))

@dp.message(Text(text='🔄Поміняти режим вікторини'))
async def change_quiz(message: types.Message):
    await message.answer("🕹<b>Виберіть режим вікторини, який вас цікавить</b>", reply_markup=keyboard_quiz.as_markup(resize_keyboard=True))

@dp.message(Text(text='Повернутися до головного меню↩️'))
async def back_main_menu(message: types.Message):
    await message.answer("📂<b>Ви були переадресовані в головне меню</b>", reply_markup=keyboard_start.as_markup(resize_keyboard=True))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())