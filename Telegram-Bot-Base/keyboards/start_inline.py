from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_keyboard = InlineKeyboardBuilder()
inline_keyboard.button(text='Inline keyboard', callback_data='callback_text')
inline_keyboard.adjust(1)