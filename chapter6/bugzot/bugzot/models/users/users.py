'''
File: users.py
Description: The file contains the definition for the user data model
             that will be used to store the information related to the
             user accounts.
'''
from bugzot.application import db
from .roles import Role


class User(db.Model):
    """User data model for storing user account information.

    The model is responsible for storing the account information on a
    per user basis and providing access to it for authentication
    purposes.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, index=True, nullable=False)
    password = db.Column(db.String(512), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    user_role = db.Column(db.Integer, db.ForeignKey(Role.id))
    role = db.relationship("Role", lazy=False)
    joining_date = db.Column(db.DateTime, nullable=False)
    last_login = db.Column(db.DateTime, nullable=False)
    account_status= db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        """User model representation."""
        return "<user {}>".format(self.username)
