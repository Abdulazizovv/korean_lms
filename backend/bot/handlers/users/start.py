from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from bot.loader import dp
from bot.keyboards.default import send_contact_btn
from bot.utils.requests_ import user_exists


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    user_id = message.from_user.id

    if user_exists(user_id).json().get('exists'):
        await message.answer("Assalomu alaykum!\n"\
                             "Bir martalik parolingizni olish uchun /login buyrug'ini bosing", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer("Assalomu alaykum!\n"\
                         "HangulHub platformasining rasmiy botiga xush kelibsiz!\n\n" \
                         "⬇️Kontaktingizni yuboring va tizimga kirish uchun bir martalik parolingizni oling(tugmani bosing)", reply_markup=send_contact_btn)



