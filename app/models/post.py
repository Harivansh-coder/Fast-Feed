from pydantic import BaseModel

class Post(BaseModel):
    message:str
    user_name:str