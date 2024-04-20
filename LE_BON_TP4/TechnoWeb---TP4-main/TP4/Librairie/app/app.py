from fastapi import FastAPI,Request,status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from app.routes.books import router as book_router
from app.routes.users import router as user_router
from starlette.staticfiles import StaticFiles
from fastapi.staticfiles import StaticFiles


templates = Jinja2Templates(directory="\TP4\Librairie\Templates")


app = FastAPI(title="My bookstore")
app.include_router(book_router)
app.include_router(user_router)

@app.get("/")
def route(request: Request):
    return RedirectResponse("./users/login", status_code= status.HTTP_303_SEE_OTHER)

app.mount("/static", StaticFiles(directory="TP4/Librairie/static"), name="static")

@app.on_event('startup')
def on_startup():
    print("Server started.")
def on_shutdown():
    print("Bye bye!")
