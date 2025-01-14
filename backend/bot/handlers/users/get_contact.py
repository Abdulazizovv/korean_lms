from aiogram import types
from bot.loader import dp
from bot.utils.requests_ import create_user


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    
    if not contact:
        return await message.answer('Iltimos, telefon raqamingizni yuboring')
    
    phone_number = contact.phone_number
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    try:
        response = create_user(
            user_id=user_id,
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            username=username
        )
    except Exception as e:
        print(e)
        return await message.answer('Siz allaqachon ro\'yxatdan o\'tgansiz\n'
                                    'Bir martalik parolni olish uchun /login buyrug\'ini bosing')
