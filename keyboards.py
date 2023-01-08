from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder

keyboard_start = ReplyKeyboardBuilder()
keyboard_start.add(types.KeyboardButton(text="🌐Головне меню"))
keyboard_start.add(types.KeyboardButton(text="🎁Получити бонус"))
keyboard_start.adjust(1)

keyboard_main = ReplyKeyboardBuilder()
keyboard_main.add(types.KeyboardButton(text='🌐Отримати інформацію'))
keyboard_main.add(types.KeyboardButton(text='❓Технічна підтримка'))
keyboard_main.add(types.KeyboardButton(text='↩️Назад'))
keyboard_main.adjust(1)

keyboard_info = ReplyKeyboardBuilder()
keyboard_info.add(types.KeyboardButton(text="📮Получити всю інформацію"))
keyboard_info.add(types.KeyboardButton(text="🆔ID користувача"))
keyboard_info.add(types.KeyboardButton(text="👤Ім'я та прізвище"))
keyboard_info.add(types.KeyboardButton(text="🌐Юзернейм"))
keyboard_info.add(types.KeyboardButton(text="🏳️Мова інтерфейсу"))
keyboard_info.add(types.KeyboardButton(text="↩️Повернутися до головного меню"))
keyboard_info.adjust(2)

keyboard_help_admin = ReplyKeyboardBuilder()
keyboard_help_admin.add(types.KeyboardButton(text="📥Зв'язатися з адміністратором через Telegram"))
keyboard_help_admin.add(types.KeyboardButton(text="❓Питання/Відповідь"))
keyboard_help_admin.add(types.KeyboardButton(text="↩️Повернутися до головного меню"))
keyboard_help_admin.adjust(1)