from aiogram import Router
from aiogram.types import CallbackQuery
from aiogram.filters import Text

router = Router()

@router.callback_query(Text("callback_text"))
async def callback_text(callback: CallbackQuery):
    await callback.answer()
    await callback.message.delete()
    await callback.message.answer('Привітик, ти натиснув на інлайн кнопку.!')