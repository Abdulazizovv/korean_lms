from aiogram import Dispatcher

from bot.loader import dp
from .throttling import ThrottlingMiddleware



def setup(dp: Dispatcher):
    dp.middleware.setup(ThrottlingMiddleware())

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
