from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .routers import auth, users
from pathlib import Path

app = FastAPI()


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

# BASE_DIR = Path(__file__).resolve().parent

@app.get("/")
async def root():
    return {"message": "feed home page"}


# auth routes
app.include_router(auth.router)

app.include_router(users.router)

@app.post("/posts/create")
async def create_post():
    return {"message": "feed page"}

