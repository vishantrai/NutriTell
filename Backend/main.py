from fastapi import FastAPI, Request, Depends, status, HTTPException
from fastapi.responses import HTMLResponse
from grpc import Status
from sqlalchemy.orm import Session
from codes.Backend import models, schemas, utils
from codes.Backend.database import SessionLocal, engine
from codes.Backend.schemas import UserCreate
# from passlib.context import CryptContext # library for password hashing
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles

# This tells FastAPI to look inside the 'templates' folder for HTML files
# templates = Jinja2Templates(directory="Backend")

# This allows you to serve CSS/JS files if needed
# app.mount("/static", StaticFiles(directory="static"), name="static")

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


# adding the users details in daatabase
@app.post("/users", status_code=status.HTTP_201_CREATED, response_class=HTMLResponse, response_model=schemas.UserOut) #status is imported from fastapi
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # hashing the password in the database
    hashed_password = utils.hash(user.password)
    user.password=hashed_password
    new_user = models.UserDetails(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# extracting a particular user detail just like we exxtract our info/profile
@app.get('/users/{id}', response_model=schemas.UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.UserDetails).filter(models.UserDetails.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=F"User with id: {id} does not exist")
    
    return user 
# in the above code we are getting a problem in which the users password is also fetched and it is not a good thing now we will solve this, for that we will make a response model beside the parameter and set what are the details of the user should come out the database
