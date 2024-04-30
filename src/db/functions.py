from typing import Union, List

from sqlalchemy import insert, select, update, and_, desc

from src.db.base import get_session
from src.db.models import User, Task


async def db_add_user(user_id: int, username: str):
    async with get_session() as session:
        user_exists = await session.get(User, user_id)
        if not user_exists:
            stmt = insert(User).values(user_id=user_id, username=username)
            await session.execute(stmt)
            await session.commit()


async def db_get_user(user_id: int) -> Union[None, User]:
    user_id = int(user_id)
    async with get_session() as session:
        query = select(User).where(User.user_id == user_id)
        result = await session.execute(query)
        answer = result.all()
        return answer[0][0] if answer else None


async def db_update_user(user_id: int, data_dict):
    async with get_session() as session:
        query = update(User).where(User.user_id == user_id).values(data_dict)
        await session.execute(query)
        await session.commit()


async def db_get_tasks(user_id: int) -> List[Task]:
    async with get_session() as session:
        query = select(Task).where(and_(Task.creator_id == user_id, Task.status == True)).order_by(desc(Task.id))
        result = await session.execute(query)
        answer = result.all()
        if answer:
            return [el[0] for el in answer]
        else:
            return []


async def db_add_task(data: dict):
    async with get_session() as session:
        query = insert(Task).values(data)
        await session.execute(query)
        await session.commit()

