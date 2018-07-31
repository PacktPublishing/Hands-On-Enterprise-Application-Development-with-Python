#!/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Date, Integer, String
from datetime import datetime

# Initialize the declarative base model
Base = declarative_base()

class Role(Base):
    __tablename__ = ‘roles’

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(length=25), nullable=False, unique=True)
    role_permissions = Column(Integer, nullable=False)

    def __repr__(self):
        return “<Role {}>”.format(role_name)
