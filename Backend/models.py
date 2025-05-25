from codes.Backend.database import Base
from sqlalchemy import Column, Integer, String, BigInteger
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import null, text


class UserDetails(Base):
    __tablename__ = 'user_details'

    id=Column(Integer, primary_key=True) 
    fullname = Column(String, nullable=False)
    username = Column(String, unique=True)
    email = Column(String, nullable=False, unique=True)
    mobile_no = Column(BigInteger, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_st = Column(TIMESTAMP(timezone = True), nullable=False, server_default=text('now()'))

