from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer("Assalomu alaykum!\n"\
                         "HangulHub platformasining rasmiy botiga xush kelibsiz!\n\n" \
                         "⬇️Kontaktingizni yuboring va tizimga kirish uchun bir martalik parolingizni oling(tugmani bosing)" )



