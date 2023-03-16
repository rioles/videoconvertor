#!/usr/bin/env python
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5

class User(BaseModel, Base):
    """ SQLAlchemy User model
    """
    __tablename__ = 'users'

    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)


if __name__=="__main__":
    print(User.__tablename__)

    for column in User.__table__.columns:
        print("{}: {}".format(column, column.type))


