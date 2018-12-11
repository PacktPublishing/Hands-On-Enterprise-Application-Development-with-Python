'''
File: models.py
Description: The models for the User service.
'''
from user_service.user_service import db
import datetime

class User(db.Model):
    """User database model.

    The User database model is used to store the information related to the individual users
    allowing for their identification and authentication.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password= db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)

    def __repr__(self):
        """Provide a representation of the Model."""
        return "<User {}>".format(self.username)

class Token(db.Model):
    """User Authetication Token Model.

    The authentication token model is used to store the authentication tokens
    for a given user which can be used to authenticate the user with the
    service.
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    auth_token = db.Column(db.String(64), nullable=False, unique=True)
    token_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())

    def __repr__(self):
        """Provide a representation of the model."""
        return "<Token {}>".format(self.id)
