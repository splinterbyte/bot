from aiogram.fsm.state import StatesGroup, State

class States(StatesGroup):
    GET_POSTNAME = State()
    GET_TEXT = State()
    GET_PHOTO = State()