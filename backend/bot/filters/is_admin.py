from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from bot.data import config


class IsAdmin(BoundFilter):
    async def check(self, message: types.Message):
        if str(message.from_user.id) in config.ADMINS:
            return True
