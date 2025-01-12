from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

send_contact_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📞Kontakt yuborish", request_contact=True)
        ]
    ],
    resize_keyboard=True
)