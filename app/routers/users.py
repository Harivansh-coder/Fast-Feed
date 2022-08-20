from fastapi import APIRouter, status, HTTPException
from ..models.user import User, UserResponse
from ..database import my_database

import uuid

router = APIRouter(
    tags=['authentication']
)


@router.post("/users/create",status_code=status.HTTP_201_CREATED, response_model= UserResponse)
async def create_user(user: User):

    for i in my_database.get_all():
        if i["user_name"] == user.user_name:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="username already taken")

    user_dict = user.dict()
    user_dict["id"] = str(uuid.uuid1())
    my_database.add_data(user_dict, user_dict["id"])
    return user_dict


# @router.get("/users")
# async def create_user():
#     user_response = my_database.get_all()
#     return user_response

    

