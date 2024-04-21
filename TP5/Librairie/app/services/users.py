from sqlalchemy import select
from uuid import uuid4
from app.database import Session
from app.models.users import User
from app.schemas.user import UserSchema

"""
def get_user_by_username(username: str):
    with Session() as session:
        statement = select(User).filter_by(username=username)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                id = user.id,
                username=user.username,
                firstname = user.firstname,
                name = user.name,
                email = user.email,
                password = user.password,
            )
    return None
"""


def get_user_by_id(id: str):
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalar(statement) 
        if user is not None:
            return UserSchema(
                id = user.id,
                username=user.username,
                firstname = user.firstname,
                name = user.name,
                email = user.email,
                password = user.password,
            )
    return None

def get_user_by_username(thisUsername :str):
    with Session() as session:
        user = session.query(User).filter(User.username == thisUsername).first()
        if user is not None:
            return UserSchema (
                id = user.id,
                username=user.username,
                firstname = user.firstname,
                name = user.name,
                email = user.email,
                password = user.password,
                admin = user.admin,
                blocked=user.blocked
            )
        return None


def register(username: str, firstname: str, name: str,email: str, password: str, confirm_your_password: str):
    # Adds a new username to the database
    maxLengthPassword = 20
    minLengthPassword = 8
    
    if password != confirm_your_password:
        raise ValueError("The passwords do not match.")
    
    elif len(password) < minLengthPassword or len(password) > maxLengthPassword:
        raise ValueError("The length of the password must be between {} and {}".format(minLengthPassword,maxLengthPassword))
    
    for user in get_all_users():
        if user["username"] == username or user["email"] == email:
            raise ValueError ("This username or email is already taken.")
    else :
        with Session() as session:
            user = User(
                id=str(uuid4()),
                username=username,
                firstname=firstname,
                name=name,
                email=email,
                password=password
            )
            session.add(user)
            session.commit()
    
def get_all_users():
    # Returns all the users as a list
    with Session() as session:
        statement = select(User)
        users = session.execute(statement).all()
        
        users_list = []
        for user in users:
            user_schema = User(
                id=user.id,
                username=user.username,
                firstname=user.firstname,
                name=user.name,
                email=user.email,
                password=user.password,
                admin =user.admin,
                blocked = user.blocked
            )
            users_list.append(user_schema)
        
        return users_list
    
def block_user(id : str):
    # Blocks the user with the given username
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one()

        user.blocked = True
        session.commit()


def unblock_user(id : str):
    # Blocks the user with the given username
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one()

        user.blocked = False
        session.commit()


def grant_admin(id : str):
    # Blocks the user with the given username
    with Session() as session:
        statement = select(User).filter_by(id=id)
        user = session.scalars(statement).one()
        #...