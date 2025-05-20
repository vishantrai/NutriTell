from .database import Base
from sqlalchemy import Column, Integer, String, BigInteger
class UserDetails(Base):
    __tablename__ = 'user_details'

    fullname = Column(String, nullable=False)
    username = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    mobile_no = Column(BigInteger, nullable=False, unique=True)
    password = Column(String, nullable=False)


