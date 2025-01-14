from .models import BotUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
import random
import string
from bot.loader import sync_bot as bot
from users.models import OneTimeCode
import logging
from bot.data.config import CHAT_ID
from threading import Thread


@receiver(post_save, sender=BotUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        print('BotUser created')
        if instance.phone_number:
            if not User.objects.filter(phone_number=instance.phone_number).exists():
                random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                user = User.objects.create_user(
                                    phone_number=instance.phone_number,
                                    first_name=instance.first_name,
                                    last_name=instance.last_name,
                                    password=random_password
                                    )
                try:
                    one_time_code = OneTimeCode.objects.get(user=user)
                    import re

                    escaped_password = re.escape(random_password)
                    escaped_code = re.escape(one_time_code.code)
                    escaped_phone_number = re.escape(instance.phone_number)

                    bot.send_message(
                        instance.user_id,
                        f"Sizning hisobingiz muvaffaqiyatli yaratildi✅\n\n"
                        f"Sizning bir martalik parolingiz: `{escaped_code}`\n\n"
                        f"Sizning hisob ma'lumotlaringiz:\n"
                        f"Login: `{escaped_phone_number}`\n"
                        f"Parol: ||{escaped_password}||\n\n"
                        f"Kirish uchun parolingizni o'zgartirishingizni tavsiya etamiz",
                        parse_mode='MarkdownV2'
                    )
                    # Send notification to chat
                    Thread(target=send_new_user_notification, args=({'user_id': instance.user_id,
                                                                    'first_name': instance.first_name,
                                                                    'last_name': instance.last_name,
                                                                    'phone_number': instance.phone_number},)).start()

                except Exception as e:
                    logging.error(f'Error while sending message to user: {e}')
            else:
                user = User.objects.get(phone_number=instance.phone_number)
                one_time_code = OneTimeCode.objects.get(user=user)
                bot.send_message(instance.user_id, 'Siz avvaldan tizimda ro\'yxatdan o\'tgansiz✅\n'
                                                   'Bir martalik parolni olish uchun /login buyrug\'ini yuboring')
            

def send_new_user_notification(data):
    user_id = data.get('user_id')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    phone_number = data.get('phone_number')
    bot.send_message(
        CHAT_ID,
        f"Yangi foydalanuvchi ro'yxatdan o'tdi✅\n\n"
        f"Foydalanuvchi ma'lumotlari:\n"
        f"Ism: {first_name}\n"
        f"Familya: {last_name}\n"
        f"Telefon raqam: {phone_number}"
    )