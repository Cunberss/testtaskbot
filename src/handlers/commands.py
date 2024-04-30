import asyncio
from datetime import datetime

from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile

from src.db import User
from src.db.functions import db_add_user, db_get_user, db_update_user, db_get_tasks
from src.fsm import CreateTask
from src.texts import main_text, create_text_tasks

router = Router(name='commands-router')


@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    await state.clear()
    await db_add_user(message.from_user.id, message.from_user.username)
    await message.answer(main_text)


@router.message(Command('add'))
async def cmd_add(message: Message, state: FSMContext):
    await state.clear()
    await state.set_state(CreateTask.title)
    await message.answer('Введи название задачи 👇')


@router.message(Command('tsk'))
async def cmd_tsk(message: Message, state: FSMContext):
    await state.clear()
    tasks = await db_get_tasks(message.from_user.id)
    if not tasks:
        await message.answer('Еще нет созданных задач')
    else:
        text = create_text_tasks(tasks)
        await message.answer(text)