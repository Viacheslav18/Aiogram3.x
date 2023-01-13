from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

def keyboard_admin_start() -> ReplyKeyboardBuilder:
    keyboard_start = ReplyKeyboardBuilder()
    keyboard_start.button(text='✅Почати користуватися ботом')
    keyboard_start.button(text='Панель адміністратора🛠')
    keyboard_start.adjust(1)
    return keyboard_start.as_markup(resize_keyboard=True)

def keyboard_admin_adminka() -> InlineKeyboardBuilder:
    keyboard_adminka = InlineKeyboardBuilder()
    keyboard_adminka.button(url='https://github.com/Viacheslav18/Aiogram3.x', text='GitHub🌐')
    keyboard_adminka.button(url='https://mastergroosha.github.io/aiogram-3-guide/', text='Aiogram 3.x by Groosha🍐')
    keyboard_adminka.adjust(1)
    return keyboard_adminka.as_markup(resize_keyboard=True)

def keyboard_admin_back() -> ReplyKeyboardBuilder:
    keyboard_back = ReplyKeyboardBuilder()
    keyboard_back.button(text='Назад↩️')
    return keyboard_back.as_markup(resize_keyboard=True)