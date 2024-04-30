from sqlalchemy import Column, String, BigInteger, DateTime, func, Integer, ForeignKey, Boolean
from src.db.base import Base


class User(Base):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String, default='Unknown')
    registration_date = Column(DateTime, default=func.now())


class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    creator_id = Column(BigInteger, ForeignKey('users.user_id'))
    create_date = Column(DateTime, default=func.now())
    title = Column(String, default='Unknown')
    description = Column(String, default='Unknown')
    status = Column(Boolean, default=True)


