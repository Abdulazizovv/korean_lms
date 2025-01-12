from .models import BotUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
import random
import string


@receiver(post_save, sender=BotUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        print('BotUser created')
        if instance.phone_number:
            if not User.objects.filter(phone_number=instance.phone_number).exists():
                random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                User.objects.create_user(
                                    phone_number=instance.phone_number,
                                    first_name=instance.first_name,
                                    last_name=instance.last_name,
                                    password=random_password
                                    )