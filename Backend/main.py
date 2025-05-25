from fastapi import FastAPI, Request, Depends, status
from fastapi.responses import HTMLResponse
from grpc import Status
from sqlalchemy.orm import Session
from codes.Backend import models, schemas, utils
from codes.Backend.database import SessionLocal, engine
from codes.Backend.schemas import UserCreate
# from passlib.context import CryptContext # library for password hashing

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

User = schemas.UserCreate

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @app.get("/register", response_class=HTMLResponse)
# def register_form(request: Request):
#     # You likely meant to use a Jinja2Template here
#     return "<h1>Registration Page (HTML template goes here)</h1>"

# @app.post("/register")
# def register_user(post: UserDetailsSchema, db: Session = Depends(get_db)):
#     new_user = models.UserDetails(
#         fullname=post.fullname,
#         username=post.username,
#         email=post.email,
#         mobile_no=post.mobile_no,
#         password=post.password
#     )

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return {"data": new_user}


@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut) #status is imported from fastapi
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # hashing the password in the database
    hashed_password = utils.hash(user.password)
    user.password=hashed_password
    new_user = models.UserDetails(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
# 