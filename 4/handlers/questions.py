from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_questions import get_keyboard

router = Router()

@router.message(Command(commands=['start']))
async def cmd_start(message: Message):
    await message.answer('Ви задоволені своїм ботом?', reply_markup=get_keyboard())

@router.message(Text(text="Так", ignore_case=True))
async def answer_yes(message: Message):
    await message.answer('Чудово!', reply_markup=ReplyKeyboardRemove())

@router.message(Text(text="Ні", ignore_case=True))
async def answer_no(message: Message):
    await message.answer('Шкода...', reply_markup=ReplyKeyboardRemove())

@router.message(Command(commands=['help']))
async def cmd_help(message: Message):
    await message.reply('<b>Список команд в боті!</b>\n\n<i>/start\n/help</i>')