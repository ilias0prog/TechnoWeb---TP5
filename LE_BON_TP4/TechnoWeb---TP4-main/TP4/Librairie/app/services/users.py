from app.database import bookstore
from app.schemas.user import UserSchema
from uuid import uuid4


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
    
    for user in get_all_users(bookstore):
        if user["username"] == username or user["email"] == email:
            raise ValueError ("This username or email is already taken.")

    newUser = {
        "id": str(uuid4()),
            "username": username,
            "firstname" : firstname,
            "name" : name,
            "password": password,    
            "email": email,
            "admin": False,
            "blocked": False,
            "connected": True
    }
    
    bookstore["users"].append(newUser)
    return 

def block_user(username: str):
    # Blocks the user with the given username
    for user in bookstore["users"]:
        if user["username"] == username:
            if user["blocked"] == True:
                raise ValueError("User is already blocked")
            else:
                user["blocked"] = True
            return
    raise ValueError("User not found")

def unblock_user(username: str):
    # Unblocks the user with the given username
    for user in bookstore["users"]:
        if user["username"] == username:
            if user["blocked"] == False:
                raise ValueError("User is already unblocked")
            else:
                user["blocked"] = False
            return
    raise ValueError("User not found")

def set_connected(username: str):
    for user in bookstore["users"]:
        if user["username"] == username:
            user["connected"] = True
            return
    raise ValueError("This user doesn't exist")
    
def set_disconnected():
    for user in bookstore["users"]:
        if user["connected"] == True :
            user["connected"] = False
            return
    raise ValueError("This user doesn't exist")

