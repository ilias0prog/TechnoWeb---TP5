from fastapi_login import LoginManager
from app.services.users import get_user_by_id

SECRET = "SECRET"
login_manager = LoginManager(SECRET, '/login', use_cookie=True)
login_manager.cookie_name = "auth_cookie"

@login_manager.user_loader()
def query_user(user_id: str):
    print(get_user_by_id(user_id))
    return get_user_by_id(user_id)
