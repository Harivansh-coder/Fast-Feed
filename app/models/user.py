from pydantic import BaseModel, EmailStr, constr

class User(BaseModel):
    name:str
    email:EmailStr
    userName:str
    password:constr(min_length=8)