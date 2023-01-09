from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard_start = ReplyKeyboardBuilder()
keyboard_start.add(types.KeyboardButton(text="🧩Вікторини"))
keyboard_start.add(types.KeyboardButton(text="⚙️Додаткові функції"))
keyboard_start.adjust(1)

keyboard_quiz = ReplyKeyboardBuilder()
keyboard_quiz.add(types.KeyboardButton(text="🌍Географічні вікторини"))
keyboard_quiz.add(types.KeyboardButton(text="⚽️Футбольні вікторини"))
keyboard_quiz.adjust(1)

keyboard_geography = ReplyKeyboardBuilder()
keyboard_geography.add(types.KeyboardButton(text="🏳️Відгадай прапор"))
keyboard_geography.add(types.KeyboardButton(text="🚫Завершити проходження вікторини"))
keyboard_geography.adjust(1)

keyboard_football = ReplyKeyboardBuilder()
keyboard_football.add(types.KeyboardButton(text="⚽️хз як назвати"))
keyboard_football.add(types.KeyboardButton(text="🚫Завершити проходження вікторини"))
keyboard_football.adjust(1)

keyboard_quiz_flag = ReplyKeyboardBuilder()
keyboard_quiz_flag.add(types.KeyboardButton(text="🏳️Відправити вікторину"))
keyboard_quiz_flag.add(types.KeyboardButton(text="🚫Завершити проходження вікторини"))
keyboard_quiz_flag.adjust(1)

keyboard_quiz_football = ReplyKeyboardBuilder()
keyboard_quiz_football.add(types.KeyboardButton(text="⚽️Відправити вікторину"))
keyboard_quiz_football.add(types.KeyboardButton(text="🚫Завершити проходження вікторини"))
keyboard_quiz_football.adjust(1)

keyboard_functions = ReplyKeyboardBuilder()
keyboard_functions.add(types.KeyboardButton(text="🧩Створити вікторину"))
keyboard_functions.adjust(1)

keyboard_functions_new_quiz = ReplyKeyboardBuilder()
keyboard_functions_new_quiz.add(types.KeyboardButton(text="🧩Створити", request_poll=types.KeyboardButtonPollType(type="quiz")))
keyboard_functions_new_quiz.add(types.KeyboardButton(text="📥Надіслати вікторину адміну бота"))
keyboard_functions_new_quiz.add(types.KeyboardButton(text="Повернутися до головного меню↩️"))
keyboard_functions_new_quiz.adjust(1)