from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Body
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from Templates import *
from app.login_manager import login_manager
import app.services.users as service
from app.schemas.user import UserSchema
from fastapi.templating import Jinja2Templates
from fastapi import Request

templates = Jinja2Templates(directory="TP5\Librairie\Templates")
router = APIRouter(prefix="/users")

@router.get("/login")
def login_form(request: Request):
    return templates.TemplateResponse("/login.html", {"request": request})
@router.post("/login")
def login_route(
        username: Annotated[str, Body()],
        password: Annotated[str, Body()]
):
    user = service.get_user_by_username(username)
    if user is None or user.password != password:
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="incorrect username or password.")
        
    access_token = login_manager.create_access_token(
        data={'sub': user.id}
    )
    
    response = JSONResponse({"status": "success"})
    response.set_cookie(
        key=login_manager.cookie_name,
        value=access_token,
        httponly=True
    )
    return response, status.HTTP_200_OK, templates.TemplateResponse("/register.html")





@router.post('/logout')
def logout_route():
    response = JSONResponse({'status': 'success'})
    response.delete_cookie(
        key=login_manager.cookie_name,
        httponly=True
    )
    return response


@router.get("/me")
def current_user_route(
    user: UserSchema = Depends(login_manager),
):
    return user

@router.get("/register")
def register_form(request: Request):
    return templates.TemplateResponse("/register.html", context={"request": request})

@router.post("/register")
def  register_action(request: Request, username: str, firstname: str, name: str,email: str, password: str, confirm_password: str):
    # Check if the user already exists in the database
    service.register(username, firstname, name, email, password, confirm_password)
    return RedirectResponse(url="/books/all", status_code=302)

#miaw