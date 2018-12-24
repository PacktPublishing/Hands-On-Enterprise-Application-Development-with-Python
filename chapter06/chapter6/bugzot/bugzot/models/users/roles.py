'''
File: roles.py
Description: The file contains the definition for the user roles model
             which will be used to assign roles to the user.
'''
from bugzot.application import db


class Role(db.Model):
    """User roles model.

    The model is responsible for storing the information about the user roles
    which is used to grant permissions to a particular action.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role_name = db.Column(db.String(50), unique=True, index=True, nullable=False)

    def __repr__(self):
        """Provide a representation for the Role model."""
        return "<Role {}>".format(self.role_name)
