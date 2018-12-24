#!/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column, ForeignKey, Date, Integer, String
from datetime import datetime

# Initialize the declarative base model
Base = declarative_base()

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, autoincrement=True)
  first_name = Column(String, nullable=False)
  last_name = Column(String, nullable=False)
  username = Column(String(length=25), unique=True, nullable=False)
  email = Column(String(length=255), unique=True, nullable=False)
  password = Column(String(length=255), nullable=False)
  date_joined = Column(Date, default=datetime.now())
  user_role = Column(Integer, ForeignKey("roles.id"))
  account_active = Column(Boolean, default=False)
  activation_key = Column(String(length=32))

  def __repr__(self):
    return "<User {}>".format(self.username)
