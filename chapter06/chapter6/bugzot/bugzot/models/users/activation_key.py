'''
File: activation_key.py
Description: The file contains the model definition for storing activation
             keys related to user accounts.
'''
from bugzot.application import db
from .users import User


class ActivationKey(db.Model):
    """Activation key model for storing activation key records for the user.

    The model is responsible for storing the records of the activation key
    on a per user basis.
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    activation_key = db.Column(db.String(64), unique=True, nullable=False)

    def __repr__(self):
        """Activation key model representation."""
        return "<ActivationKey {}>".format(self.user_id)
