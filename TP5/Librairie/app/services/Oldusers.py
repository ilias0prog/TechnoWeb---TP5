from app.database import bookstore
from app.schemas.user import UserSchema
from uuid import uuid4
from sqlalchemy import select

from app.database import Session
from app.models.users import User
from app.schemas import UserSchema

def get_all_users(bookstore):
    # Returns all the users as a list
    return bookstore["users"]

def get_user_by_username(username: str):
    for user in bookstore['users']:
        if user['username'] == username:
            return UserSchema.model_validate(user)
    return None


def get_user_by_id(id: str):
    for user in bookstore['users']:
        if user['id'] == id:
            return UserSchema.model_validate(user)
    return None


def register(username: str, firstname: str, name: str,email: str, password: str, confirm_your_password: str):
    # Adds a new username to the database
    maxLengthPassword = 20
    minLengthPassword = 8
    
    if password != confirm_your_password:
        raise ValueError("The passwords do not match.")
    
    if len(password) < minLengthPassword or len(password) > maxLengthPassword:
        raise ValueError("The length of the password must be between {} and {}".format(minLengthPassword,maxLengthPassword))
    
    for user in get_all_users():
        if user["username"] == username or user["email"] == email:
            raise ValueError ("This username or email is already taken.")

    newUser = {
        "id": str(uuid4()),
            "username": username,
            "firstname" : firstname,
            "name" : name,
            "password": password,    
            "email": email,
            "admin": False
    }
    
    bookstore["users"].append(newUser)
    return 