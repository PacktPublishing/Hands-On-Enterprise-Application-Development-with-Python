'''
File: __init__.py
Description: Bugzot application entrypoint file.
'''
from .application import app, bcrypt, db
from bugzot.models import ActivationKey, Category, Component, Product, Role, User, Version

db.create_all()
