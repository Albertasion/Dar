from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMProfile(StatesGroup):
    name = State()
    photo = State()
    age = State()
    # gender = State()
    # hobby = State()