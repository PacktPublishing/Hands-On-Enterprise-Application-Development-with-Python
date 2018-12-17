'''
File: application.py
Description: The file contains the application initialization
             logic that is used to serve the application.
'''
from flask import Flask, session
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

# Initialize our Flask application
app = Flask(__name__, instance_relative_config=True)

# Let's read the configuration
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Let's setup the database
db = SQLAlchemy(app)

# Initializing the security configuration
bcrypt = Bcrypt(app)

# We will require sessions to store user activity across the application
Session(app)

from bugzot.models import User, Product

@app.route('/ping', methods=['GET'])
def ping():
    '''Output a pong response as a greeting.'''

    return "Pong", 200
