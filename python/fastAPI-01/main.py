from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Users(BaseModel):
    id:int
    name:str
    email:str
    age:int

users: List[Users] = []

@app.get("/")
def response_message():
    return {"Message":"Wellcome to python server"}

@app.get("/users")
def response_users():
    return {"data":users}