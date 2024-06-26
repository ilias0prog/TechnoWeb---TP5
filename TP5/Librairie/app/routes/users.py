from typing import Annotated
from fastapi import APIRouter, HTTPException, status, Depends, Form
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.responses import JSONResponse
from Templates import *
from app.login_manager import *
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
def login_route( username: Annotated[str, Form()], password: Annotated[str,Form()]):
    
    user = service.get_user_by_username(username)
    if user is not None:
        if user.blocked:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User is blocked."
            )
        if user.password != password:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="incorrect password.")
        
        access_token = login_manager.create_access_token(
            data={'sub': user.id}
        )
        response = RedirectResponse(url="/books/all", status_code=302)
        response.set_cookie(
            key=login_manager.cookie_name,
            value=access_token,
            httponly=True
        )
        return response



@router.get("/logout/")
def logout_form(request: Request):
    return templates.TemplateResponse("/logout.html", {"request": request })

@router.post('/logout/')
def logout_route():
    response = RedirectResponse(url="/users/login", status_code=302)
    response.delete_cookie(
        key=login_manager.cookie_name,
        httponly=True
    )
  
    return response


@router.get("/me")
def current_user_route(request : Request, user: UserSchema = Depends(login_manager)):
    
    return templates.TemplateResponse("user.html", context={"request": request,"user": user})





@router.get("/register")
def register_form(request: Request):
    return templates.TemplateResponse("/register.html", context={"request": request})

@router.post("/register")
def  register_action( username:Annotated[str, Form()], firstname: Annotated[str, Form()], name:Annotated[str, Form()],email:Annotated[str, Form()], password: Annotated[str, Form()], confirm_password: Annotated[str, Form()]):
    service.register(username, firstname, name, email, password, confirm_password)
    response = RedirectResponse(url="/books/all", status_code=302)
    return  response


@router.get("/admin")
def admin_form(request: Request):
    return templates.TemplateResponse("/admin.html", context={"request": request, "users": service.get_all_users()})

@router.get("/block/{username}")
def block_form(request: Request, username : str):
    service.get_all_users() 
    return templates.TemplateResponse("/block_confirmation.html", context={"request": request, "username" : username})


@router.post("/block/{username}")
def block_user(username: str) :
    service.block_user(username)
    response = RedirectResponse(url="/books/all", status_code=302)
    return  response

@router.get("/unblock/{username}")
def unblock_form(request: Request, username : str):
    service.get_all_users() 
    return templates.TemplateResponse("/unblock_confirmation.html", context={"request": request, "username" : username})


@router.post("/unblock/{username}")
def unblock_user(username: str) :
    service.unblock_user(username)
    response = RedirectResponse(url="/books/all", status_code=302)
    return  response