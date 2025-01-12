from aiogram.dispatcher.filters.state import StatesGroup, State


class Mailing(StatesGroup):
    text = State()
    state = State()
    photo = State()