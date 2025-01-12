from aiogram import types
from bot.loader import dp


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    await message.answer(f"📞 Sizning raqamingiz: {contact.phone_number}\n"
                         f"📝 Sizning ismingiz: {contact.first_name}\n"
                         f"📝 Sizning familiyangiz: {contact.last_name}\n"
                         f"🔑 Parolingiz: 123456")