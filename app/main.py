from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi.params import Body
# from typing import Optional, List
# from random import randrange
from . import models
from .database import engine
from .routers import post ,user,auth , vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

origins =  ['*']    #['*'] for all the origins making it public


app = FastAPI()  
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers= ['*'],
) 

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World!!!!"}





