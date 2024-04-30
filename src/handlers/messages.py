from aiogram import Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from src.db.functions import db_add_task
from src.fsm import CreateTask


router = Router(name='client-messages-router')


@router.message(StateFilter(CreateTask.title))
async def create_task_title_handler(message: Message, state: FSMContext):
    title = message.text
    if len(title) > 50 or len(title) < 5:
        await message.answer('Название задачи должно быть от 5 до 50 символов, попробуй еще раз 👇')
    else:
        await state.update_data(title=title)
        await state.set_state(CreateTask.description)
        await message.answer('Отправь описание к задаче 👇')


@router.message(StateFilter(CreateTask.description))
async def create_task_description_handler(message: Message, state: FSMContext):
    description = message.text
    if len(description) > 200 or len(description) < 8:
        await message.answer('Описание к задаче должно быть от 8 до 200 символов, попробуй еще раз 👇')
    else:
        state_data = await state.get_data()
        data = {'creator_id': message.from_user.id,
                'title': state_data['title'],
                'description': description}
        await db_add_task(data)
        await message.answer('Задача успешно создана ✅')
        await state.clear()