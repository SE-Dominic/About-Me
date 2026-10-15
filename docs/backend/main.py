from fastapi import FastAPI, Form, HTTPException
from typing import Annotated
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import smtplib, os
from email.message import EmailMessage

app = FastAPI()
load_dotenv()

email = "dominic.allen998@gmail.com"
password = os.getenv("EMAIL_PASSWORD")
sender = os.getenv("SENDER")


#add CORS Middleware here vvv
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:8000", "https://127.0.0.1:5501"],  # your frontend origin(s)
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)

#pydantic model for form
class UserContactData(BaseModel):
    name: str
    email:str
    message: str

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/contact")
def receiveContact(data: Annotated[UserContactData, Form()]):
    if not email or not sender or not password:
        raise HTTPException(status_code=500, detail="Email settings are not configured")

    emailMessage = EmailMessage()
    emailMessage["Subject"] = f"Contact Form: {data.name}"
    emailMessage["From"] = sender
    emailMessage["To"] = email
    emailMessage["Reply-To"] = data.email
    emailMessage.set_content(
        f"Name: {data.name}\n"
        f"Email: {data.email}\n\n"
        f"Message:\n{data.message}"
    )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(sender, password)
            server.send_message(emailMessage, from_addr=sender, to_addrs=[email])
            return {"email-status": "successful"}
    except (smtplib.SMTPException, OSError) as e:
        raise HTTPException(status_code=502, detail="Email delivery failed") from e