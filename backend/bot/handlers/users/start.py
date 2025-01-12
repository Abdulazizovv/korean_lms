from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # salomlashish xabari
    await message.answer(f"Salom, {message.from_user.id}!")



