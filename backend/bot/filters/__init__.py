from aiogram import Dispatcher

from bot.loader import dp
from .is_admin import IsAdmin
from .is_group import IsGroup


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsAdmin)
    dp.filters_factory.bind(IsGroup)
    pass


if __name__ == "filters":
    # dp.filters_factory.bind(IsAdmin)
    pass