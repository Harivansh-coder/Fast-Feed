from fastapi import Request, Depends, APIRouter, HTTPException, status
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from ..database import my_database
from ..utils import hash

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

    user = my_database.get_one(data.username)    

    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"invalid credentials")

    if user["password"] != data.password:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"invalid credentials")

    print(user["id"])
    # access_token = oauth2.create_access_token(data={'user_id': user.id})

    # return {"access_token": access_token, "token_type": "bearer"}