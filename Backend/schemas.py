from pydantic import BaseModel, EmailStr
from datetime import datetime

# Pydantic schema for creating the data in the database
#request model
class UserCreate(BaseModel):
    fullname: str
    username: str
    email: EmailStr
    mobile_no: int
    password: str

    

# we are getting a problem in which whatever the details user is putting to register himself in response he is getting all the details which we dont want we want to give only selected data as output so we are going to define a response model

# response model
class UserOut(BaseModel):
    
    id: int
    fullname: str
    username: str
    email: str
    created_st: datetime
    class Config:
        from_attributes = True