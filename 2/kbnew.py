from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard_start = ReplyKeyboardBuilder()
keyboard_start.add(types.KeyboardButton(text="Пройти тест на токсіка😈"))
keyboard_start.adjust(1)

keyboard_toksik_checker = ReplyKeyboardBuilder()
keyboard_toksik_checker.add(types.KeyboardButton(text="Так, я токсік😈"))
keyboard_toksik_checker.add(types.KeyboardButton(text="Ні, я дуже добра душа😇"))
keyboard_toksik_checker.adjust(2)