from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def keyboard_user_start() -> ReplyKeyboardBuilder:
    keyboard_start = ReplyKeyboardBuilder()
    keyboard_start.button(text='✅Почати користуватися ботом')
    return keyboard_start.as_markup(resize_keyboard=True)