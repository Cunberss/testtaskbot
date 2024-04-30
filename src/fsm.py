from aiogram.fsm.state import StatesGroup, State


class CreateTask(StatesGroup):
    title = State()
    description = State()
