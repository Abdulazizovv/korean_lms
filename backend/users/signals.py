from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Profile, OneTimeCode
import logging


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        OneTimeCode.objects.create(user=instance)
        Profile.objects.create(user=instance)
        logging.info(f'Profile created for {instance.phone_number}')


@receiver(post_save, sender=OneTimeCode)
def create_new_code(sender, instance, created, **kwargs):
    if created:
        print(f'New code created for {instance.user.phone_number}')
    else:
        if instance.is_used and not OneTimeCode.objects.filter(user=instance.user, is_used=False).exists():
            print(f'Code {instance.code} has been used')
            OneTimeCode.objects.create(user=instance.user)