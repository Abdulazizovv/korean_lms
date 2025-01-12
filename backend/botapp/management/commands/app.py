from aiogram import executor
from django.core.management.base import BaseCommand


from  bot import filters
from bot import middlewares,handlers

from bot.loader import dp
from bot.utils.notify_admins import on_startup_notify
from bot.utils.set_bot_commands import set_default_commands


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        pass


async def on_startup(dispatcher):
    filters.setup(dp)
    middlewares.setup(dp)
    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


executor.start_polling(dp, on_startup=on_startup, skip_updates=True, fast=True)
