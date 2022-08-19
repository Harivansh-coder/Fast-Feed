from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name:str
    email:EmailStr
    userName:str
    password:str(min_length=8)