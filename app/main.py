from fastapi import FastAPI, Request, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, users
from fastapi.templating import Jinja2Templates
from pathlib import Path
from .utils.oauth2 import get_current_user
import socketio



app = FastAPI()

sio = socketio.AsyncServer(async_mode="asgi")
socket_app = socketio.ASGIApp(sio, app)


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))


@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def message(sid, data):
    await sio.emit('post_message', data)



@sio.event
def disconnect(sid):
    print('disconnect ', sid)



@app.get("/")
async def root(request: Request):
    cookie_token: str = request.cookies.get("AccessToken")

    if not cookie_token:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not Authenticated"
        )

    context = {'request': request, "current_user": get_current_user(cookie_token)['user_name']}
    return templates.TemplateResponse("index.html", context)



# auth routes
app.include_router(auth.router)
# user routes
app.include_router(users.router)



