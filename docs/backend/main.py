from fastapi import FastAPI, Form #for FastAPI framework
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

#add CORS Middleware here vvv

#pydantic model for form
class UserContactData(BaseModel):
    name: str
    email:str
    message: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/contact")
async def receiveContact(data: Annotated[UserContactData, Form()]):
    return {"user": data}