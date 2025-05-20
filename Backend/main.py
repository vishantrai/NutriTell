from fastapi import *
from fastapi.responses import HTMLResponse
import psycopg2
from . import models
from models import UserDetails
from sqlalchemy.orm import Session
from .database import *

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/register", response_class = HTMLResponse)
def register_form(request: Request):
    return ("register.html", {"request": request})

@app.post("/register")
def register_user(post: UserDetails, db: Session = Depends(get_db)):
    new_post = models.UserDetails(fullname=UserDetails.fullname, username=UserDetails.username,email=UserDetails.email, mobile_no=UserDetails.mobile_no, password=UserDetails.password)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return{"data":new_post}
