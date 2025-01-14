from aiogram import types
from aiogram.dispatcher.filters import Command
from bot.loader import dp
from bot.keyboards.default import send_contact_btn
from bot.utils.requests_ import user_exists
from bot.utils.requests_ import get_one_time_code, get_user


@dp.message_handler(Command('login'))
async def bot_login(message: types.Message):
    user_id = message.from_user.id
    if not user_exists(user_id).json().get('exists'):
        await message.answer("Siz ro\'yxatdan o\'tmagansiz\n"
                             "Parolni olish uchun telefon raqamingizni yuboring", reply_markup=send_contact_btn)
    else:
        bot_user = get_user(user_id).json()
        print(bot_user)
        if bot_user.get('is_active') and bot_user.get('phone_number'):
            otp = get_one_time_code(bot_user.get('phone_number'))
            await message.answer(f"Bir martalik parolingiz: `{otp.json().get('code')}`", parse_mode='Markdownv2')
        else:
            await message.answer('Siz ro\'yxatdan o\'tmagansiz\n'
                                 'Telefon raqamingizni yuboring', reply_markup=send_contact_btn)