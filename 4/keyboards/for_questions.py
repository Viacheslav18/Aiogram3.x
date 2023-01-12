from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_keyboard() -> ReplyKeyboardBuilder:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text="Так")
    keyboard.button(text="Ні")
    keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)