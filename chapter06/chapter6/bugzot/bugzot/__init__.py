'''
File: __init__.py
Description: Bugzot application entrypoint file.
'''
from .application import app, bcrypt, db
from bugzot.models import ActivationKey, Category, Component, Product, Role, User, Version
from bugzot.views import IndexView

# Define the routes
app.add_url_rule('/', view_func=IndexView.as_view('index_view'))

# Migrate the database
db.create_all()
