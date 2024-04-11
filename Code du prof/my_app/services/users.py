from sqlalchemy import select

from my_app.database import Session
from my_app.models.users import User
from my_app.schemas import UserSchema


def get_user_by_username(username: str):
    with Session() as session:
        statement = select(User).filter_by(username=username)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                id=user.id,
                username=user.username,
                password=user.password,
            )
    return None


def get_user_by_id(id: str):
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                id=user.id,
                username=user.username,
                password=user.password,
            )
    return None
