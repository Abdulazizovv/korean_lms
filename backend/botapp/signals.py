from .models import BotUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
import random
import string
from bot.loader import sync_bot as bot
from users.models import OneTimeCode
import logging


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
                one_time_code = OneTimeCode.objects.get(user=user)
                try:
                    bot.send_message(instance.user_id, f'Sizning hisobingiz muvaffaqiyatli yaratildi✅\n\n'
                                                    f'Sizning bir martalik parolingiz: {one_time_code}\n\n'
                                                    f'Sizning hisob ma\'lumotlaringiz:\n'
                                                    f'Login: {instance.phone_number}\n'
                                                    f'Parol: {random_password}\n'
                                                    f'Kirish uchun parolingizni o\'zgartirishingizni tavsiya etamiz.')
                except Exception as e:
                    logging.error(f'Error while sending message to user: {instance}')