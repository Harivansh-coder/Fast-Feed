from fastapi import Request, Depends, APIRouter, HTTPException, status, Response
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.security import OAuth2PasswordRequestForm
from ..database import my_database
from ..utils import oauth2

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

    access_token = oauth2.create_access_token(data={'user_id': user["id"]})

    print(user["id"])
    print()
    # access_token = oauth2.create_access_token(data={'user_id': user.id})

    # return {"access_token": access_token, "token_type": "bearer"}

    response = RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)
    response.set_cookie(key = "AccessToken", value= access_token)
    return response

@router.get("/logout")
def logout(response : Response):
  response = RedirectResponse('/login', status_code= 302)
  response.delete_cookie(key ='AccessToken')
  return response





# @router.post('/login')
# async def sign_in(
#         user_data: OAuth2PasswordRequestForm = Depends(),
#         service: AuthService = Depends(),
# ):
#     session = await service.authenticate_user(
#         user_data.username,
#         user_data.password
#     )
#     response = RedirectResponse(url='/')
#     response.set_cookie('Authorization', value=session['session_id'], httponly=True)
#     return response


# async def get_current_user(request: Request): 
#     try:
#         cookie_authorization: str = request.cookies.get("Authorization")
#         # some logic with cookie_authorization
#     except Exception as e:
#         raise HTTPException(
#             status_code=status.HTTP_403_FORBIDDEN, detail="Invalid authentication"
#         )