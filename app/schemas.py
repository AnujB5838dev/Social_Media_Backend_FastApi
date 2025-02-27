from pydantic import BaseModel, EmailStr   #use for defining rules for posting data, for example when frontend sends data to backend
from datetime import datetime
from typing import Optional
from pydantic.types import conint 



# schema for user creation
class UserCreate(BaseModel):
    email : EmailStr
    password: str

# response model for user creation
class UserOut(BaseModel):
    id : int
    email : EmailStr
    created_at:datetime                                       

    class Config:
        from_attributes = True



# user login schemas
class UserLogin(BaseModel):
    email: EmailStr
    password: str






class PostBase(BaseModel):
    title: str
    content:str
    published:bool = True
    

class PostCreate(PostBase):
    pass


# This is response model for post
class Post(PostBase):
    id : int
    # title: str     #dont need to add bcoz it is now extending postbase class
    # content:str      #dont need to add bcoz it is now extending postbase class
    # published:bool     #dont need to add bcoz it is now extending postbase class
    created_at: datetime
    owner_id : int
    owner : UserOut


    class Config:
        from_attributes = True



class PostOut(BaseModel):
    Post : Post
    votes: int

    class Config:
        from_attributes = True




# response model for user login
class Token(BaseModel):
    access_token : str
    token_type : str


class TokenData(BaseModel):
    id : Optional[str] = None




class Vote(BaseModel):
    post_id: int
    dir : conint(le=1)