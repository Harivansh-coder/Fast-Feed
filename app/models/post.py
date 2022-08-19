from pydantic import BaseModel

class Post(BaseModel):
    message:str
    userName:str