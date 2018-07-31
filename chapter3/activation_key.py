#!/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Date, Integer, String
from datetime import datetime

# Initialize the declarative base model
Base = declarative_base()

class ActivationKey(Base):
    __tablename__ = ‘activation_keys’

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey(users.id))
    activation_key = Column(String(length=32), nullable=False)

    def __repr__(self):
        return “<ActivationKey {}>”.format(self.id)
