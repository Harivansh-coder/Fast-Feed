from pydantic import BaseModel, constr

class User(BaseModel):
    user_name: str
    password:constr(min_length=8)


class UserResponse(BaseModel):
    id: str 
    user_name: str
