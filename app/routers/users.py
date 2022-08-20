from fastapi import APIRouter, status, HTTPException
from ..models.user import User, UserResponse
from ..database import my_database
import uuid

router = APIRouter(
    prefix="/users",
    tags=["users"]
)



@router.post("/create",status_code=status.HTTP_201_CREATED, response_model= UserResponse)
async def create_user(user: User):

    if my_database.get_one(user.user_name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="username already taken")

    user_dict = user.dict()
    user_dict["id"] = str(uuid.uuid1())
    my_database.add_data(user_dict, user_dict["id"])
    return user_dict


@router.get("/")
async def create_user():
    user_response = my_database.get_all()
    return user_response

    

