from fastapi import Request, Depends, APIRouter
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(
    tags=['authentication']
)

BASE_DIR = Path(__file__).resolve().parent.parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))



@router.get("/login", response_class=HTMLResponse)
def login(request: Request):
   print(str(Path(BASE_DIR, 'templates')))
   context = {'request': request, }
   return templates.TemplateResponse("login.html", context)


@router.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    return {
    "username": data.username,
    "password":data.password,
   }