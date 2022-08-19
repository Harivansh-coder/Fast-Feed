from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from pathlib import Path


app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent


templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@app.get("/")
async def root():
    return {"message": "feed home page"}


@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
   context = {'request': request, }
   return templates.TemplateResponse("login.html", context)


@app.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
   return {
    "username": data.username,
    "password":data.password,
   }

@app.post("/posts/create")
async def create_post():
    return {"message": "feed page"}

@app.post("/users/create")
async def create_user(request: Request):
    context = {'request': request, }
    return templates.TemplateResponse("create.html", context)
    
@app.get("/users/create")
async def create_user(request: Request):
    context = {'request': request, }
    return templates.TemplateResponse("create.html", context)
