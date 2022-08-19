from fastapi import Request, Depends, APIRouter, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path
from ..models.user import User

router = APIRouter(
    tags=['authentication']
)


@router.post("/users/create")
async def create_user(user: User):
    return {
        "message": "created"
    }
    

