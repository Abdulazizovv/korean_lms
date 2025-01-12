from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from bot.data import config


class IsGroup(BoundFilter):
    async def check(self, message: types.Message):
        if message.chat.type == 'group' or message.chat.type == 'supergroup':
            return True
